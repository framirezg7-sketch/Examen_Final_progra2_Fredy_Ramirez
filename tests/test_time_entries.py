"""Pruebas de persistencia para TimeEntry (Ficha 21 - RAMÍREZ GÓMEZ, FREDY ALEXANDER).

Cubre:
- T1: crear un registro con una sesión, cerrarla, abrir sesión nueva y verificar que
      el registro y total_minutes siguen presentes.
- T2: dos registros de 45 y 30 min → total_minutes == 75.
- T3: CHECK constraint de minutes (0 ó 481) provoca IntegrityError.
- T4: la FK de ticket_id rechaza un ticket inexistente (IntegrityError).
- T5: fecha futura persiste en el repositorio (es una regla del servicio, no del DDL).

Todas las pruebas usan las fixtures de conftest.py:
- committed_db  → confirma de verdad; se usa para T1 (sesión nueva).
- db            → savepoint por prueba, rollback al final; para T2–T5.

No se modifica ninguna prueba existente.
"""

from __future__ import annotations

from datetime import date, timedelta

import pytest
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.database import create_app_engine
from app.models.time_entry import TimeEntry
from app.repositories.sqlalchemy import SqlAlchemyTimeEntryRepository
from tests.conftest import TEST_DATABASE_URL


# ---------------------------------------------------------------------------
# Helpers locales
# ---------------------------------------------------------------------------

def _seed_ids(session: Session) -> tuple[int, int]:
    """Devuelve (ticket_id, technician_id) del primer técnico y su ticket del seed."""
    tech_id: int = session.scalar(
        text("SELECT id FROM users WHERE role = 'technician' LIMIT 1")
    )
    ticket_id: int = session.scalar(text("SELECT id FROM tickets LIMIT 1"))
    return ticket_id, tech_id


def _count_entries(session: Session) -> int:
    return session.scalar(text("SELECT COUNT(*) FROM time_entries"))


# ---------------------------------------------------------------------------
# T1 · Crear y leer desde sesión nueva (committed_db)
# ---------------------------------------------------------------------------

@pytest.mark.integration
def test_create_and_read_in_new_session(committed_db):
    """Un registro guardado con commit() persiste al abrir una sesión nueva."""
    engine = create_app_engine(TEST_DATABASE_URL)

    # Sesión 1: insertar
    with Session(engine) as session1:
        ticket_id, tech_id = _seed_ids(session1)
        repo = SqlAlchemyTimeEntryRepository(session1)
        entry = TimeEntry(
            ticket_id=ticket_id,
            technician_id=tech_id,
            minutes=45,
            description="Cambio de tóner y limpieza de rodillo",
            worked_on=date.today(),
        )
        saved = repo.create(entry)
        assert saved.id is not None, "El repositorio debe asignar el id"
        session1.commit()
        saved_id = saved.id

    # Sesión 2: leer sin caché
    with Session(engine) as session2:
        repo2 = SqlAlchemyTimeEntryRepository(session2)
        entries = repo2.list_by_ticket(ticket_id)
        ids = [e.id for e in entries]
        assert saved_id in ids, "El registro debe seguir en la base tras cerrar la sesión"
        total = repo2.total_minutes(ticket_id)
        assert total == 45

    engine.dispose()


# ---------------------------------------------------------------------------
# T2 · Dos registros → total acumulado correcto (db — savepoint)
# ---------------------------------------------------------------------------

@pytest.mark.integration
def test_two_entries_total_minutes(db):
    """45 min + 30 min = 75 min de total."""
    ticket_id, tech_id = _seed_ids(db)
    repo = SqlAlchemyTimeEntryRepository(db)

    repo.create(TimeEntry(
        ticket_id=ticket_id, technician_id=tech_id,
        minutes=45, description="Primera tarea", worked_on=date.today(),
    ))
    repo.create(TimeEntry(
        ticket_id=ticket_id, technician_id=tech_id,
        minutes=30, description="Segunda tarea",
        worked_on=date.today() - timedelta(days=1),
    ))

    assert repo.total_minutes(ticket_id) == 75
    entries = repo.list_by_ticket(ticket_id)
    assert len(entries) == 2
    # La más antigua (worked_on anterior) debe aparecer primero.
    assert entries[0].worked_on <= entries[1].worked_on


# ---------------------------------------------------------------------------
# T3 · CHECK constraint: minutes fuera del rango [1, 480]
# ---------------------------------------------------------------------------

@pytest.mark.integration
@pytest.mark.parametrize("bad_minutes", [0, 481, -1])
def test_check_constraint_minutes(db, bad_minutes):
    """minutes = 0, 481 ó -1 deben ser rechazados por la base con IntegrityError."""
    ticket_id, tech_id = _seed_ids(db)

    before = _count_entries(db)

    with pytest.raises(IntegrityError):
        db.execute(
            text(
                "INSERT INTO time_entries "
                "(ticket_id, technician_id, minutes, description, worked_on, created_at) "
                "VALUES (:tid, :uid, :m, 'test', CURRENT_DATE, NOW())"
            ),
            {"tid": ticket_id, "uid": tech_id, "m": bad_minutes},
        )
        db.flush()

    db.rollback()
    after = _count_entries(db)
    assert after == before, "El CHECK no debe crear la fila"


# ---------------------------------------------------------------------------
# T4 · FK ticket_id: ticket inexistente es rechazado
# ---------------------------------------------------------------------------

@pytest.mark.integration
def test_fk_rejects_nonexistent_ticket(db):
    """Un ticket_id que no existe en la tabla tickets viola la FK."""
    _, tech_id = _seed_ids(db)
    before = _count_entries(db)

    with pytest.raises(IntegrityError):
        db.execute(
            text(
                "INSERT INTO time_entries "
                "(ticket_id, technician_id, minutes, description, worked_on, created_at) "
                "VALUES (:tid, :uid, 60, 'test FK', CURRENT_DATE, NOW())"
            ),
            {"tid": 999999, "uid": tech_id},
        )
        db.flush()

    db.rollback()
    assert _count_entries(db) == before


# ---------------------------------------------------------------------------
# T5 · Fecha futura: el repositorio persiste (la regla es del servicio)
# ---------------------------------------------------------------------------

@pytest.mark.integration
def test_future_date_persists_at_repository_level(db):
    """El CHECK del DDL no prohíbe fechas futuras; esa validación es del servicio."""
    ticket_id, tech_id = _seed_ids(db)
    repo = SqlAlchemyTimeEntryRepository(db)

    future = date.today() + timedelta(days=7)
    entry = repo.create(TimeEntry(
        ticket_id=ticket_id, technician_id=tech_id,
        minutes=60, description="Fecha futura — validar en servicio",
        worked_on=future,
    ))
    assert entry.id is not None
    entries = repo.list_by_ticket(ticket_id)
    assert any(e.worked_on == future for e in entries)


# ---------------------------------------------------------------------------
# T6 · total_minutes == 0 cuando no hay registros
# ---------------------------------------------------------------------------

@pytest.mark.integration
def test_total_minutes_zero_when_no_entries(db):
    """total_minutes devuelve 0, no None, cuando el ticket no tiene registros."""
    ticket_id, _ = _seed_ids(db)
    repo = SqlAlchemyTimeEntryRepository(db)
    # Sin insertar nada, el seed puede traer datos; buscamos un ticket diferente.
    # Usamos el id más alto del seed + 1 para garantizar cero entradas.
    max_id: int = db.scalar(text("SELECT MAX(id) FROM tickets"))
    # Creamos un ticket real para satisfacer la FK.
    requester_id: int = db.scalar(
        text("SELECT id FROM users WHERE role = 'requester' LIMIT 1")
    )
    new_ticket_id: int = db.scalar(
        text(
            "INSERT INTO tickets (title, description, category, priority, status, "
            "requester_id, created_at, updated_at, due_at) "
            "VALUES ('T-zero', 'desc', 'General', 'Low', 'open', "
            ":rid, NOW(), NOW(), NOW() + INTERVAL '1 day') RETURNING id"
        ),
        {"rid": requester_id},
    )
    assert repo.total_minutes(new_ticket_id) == 0
