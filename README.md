# Examen Final - Programación II · HelpDesk EDU
**Serie II: Módulo Time Entries (Registro de tiempo trabajado)**

---

## 📋 Identificación

- **Estudiante:** RAMÍREZ GÓMEZ, FREDY ALEXANDER
- **Carné:** 23-15803
- **Módulo asignado:** Ficha 21 – Tiempo trabajado con fecha válida
- **Repositorio:** [https://github.com/framirezg7-sketch/Examen_Final_progra2_Fredy_Ramirez](https://github.com/framirezg7-sketch/Examen_Final_progra2_Fredy_Ramirez)

---

## 🎯 Alcance implementado (Fase 1 completada)

### ✅ Entidad y persistencia

- **Dataclass de dominio:** `app/models/time_entry.py`
  - Campos: `id`, `ticket_id`, `technician_id`, `minutes` (1–480), `description`, `worked_on` (DATE), `created_at`
  - Patrón idéntico a `Comment`: `id = None` hasta que el repositorio persiste

- **ORM y DDL:**
  - `TimeEntryORM` en `app/repositories/sqlalchemy.py` con `CheckConstraint` para `minutes`
  - Tabla `time_entries` en `docs/database/database.sql` con FK CASCADE a `tickets` y `users`
  - Índice `idx_time_entries_ticket`

- **Relaciones:**
  - `Ticket.time_entries` con `back_populates`, `cascade="all, delete-orphan"`, orden por `worked_on, created_at`
  - Soporte en `InMemoryTicketRepository` (contador `_next_time_entry_id`)

- **Repositorio:**
  - `SqlAlchemyTimeEntryRepository` con:
    - `create(entry)` → inserta y asigna id
    - `list_by_ticket(ticket_id)` → ordenado por fecha
    - `total_minutes(ticket_id)` → SUM en SQL, devuelve 0 si no hay registros

- **Pruebas:** `tests/test_time_entries.py` (8 pruebas)
  - T1: crear y leer desde sesión nueva (`committed_db`)
  - T2: dos registros → total 75 min
  - T3: CHECK constraint rechaza minutes 0, 481, -1
  - T4: FK rechaza ticket inexistente
  - T5: fecha futura persiste (regla del servicio, no del DDL)
  - T6: total_minutes == 0 cuando no hay registros

---

## 📊 Resultados de pruebas

### Pruebas unitarias (sin PostgreSQL)

```
tests/test_week07_models.py .................. PASSED (31/31)
tests/test_week08_relations.py ............... PASSED
tests/test_week09_architecture.py ............ PASSED
```

**Total: 31/31 ✅** — sin romper ninguna prueba existente.

### Pruebas de integración (PostgreSQL)

```
tests/test_time_entries.py ................... SKIPPED (8/8)
tests/test_week11_persistence.py ............. SKIPPED
tests/test_week13_repository_contract.py ..... SKIPPED
```

**Estado:** PostgreSQL no disponible en el entorno local (puerto 5433).  
Las pruebas usan el fixture `committed_db` / `db` que intentan conectar a `helpdesk_test` y hacen `pytest.skip()` cuando la base no responde.

**Nota:** La implementación está lista para ejecutarse contra `helpdesk_test` cuando PostgreSQL esté disponible. Todas las guardias de seguridad (`assert_is_test_database`, `TEST_DATABASE_URL`) están activas.

---

## 🌳 Estructura de ramas

### `main`
Base del proyecto (semana 17 del curso). Sin cambios propios del examen.

### `dev`
Rama de integración con 2 commits:
1. **docs:** Propuesta Time Entries + documentos del examen (Serie II)
2. **merge:** Integración de `feature/time-entries-model` (fase 1)

### `feature/time-entries-model`
Implementación completa de entidad y persistencia (1 commit):
```
feat(time-entries): entidad TimeEntry, relaciones y repositorio con pruebas de persistencia
```

**Archivos modificados:**
- `app/models/entities.py` — añadido `time_entries: list[TimeEntry]` al dataclass `Ticket`
- `app/repositories/sqlalchemy.py` — `TimeEntryORM` + repositorio + `_ticket_to_domain` actualizado
- `app/repositories/memory.py` — soporte para `time_entries` en `update()`
- `docs/database/database.sql` — DDL de `time_entries`

**Archivos nuevos:**
- `app/models/time_entry.py`
- `tests/test_time_entries.py`

---

## 📦 Pendiente de implementación

### Fase 2: Servicio y API
- [ ] `TicketService.add_time_entry()` con validación de reglas (R1–R8)
- [ ] Endpoints `/api/tickets/{id}/time-entries` (POST, GET)
- [ ] Esquemas Pydantic: `TimeEntryCreate`, `TimeEntryOut`, `TimeEntrySummary`
- [ ] Pruebas de servicio y API

### Fase 3: Pantalla (cliente web)
- [ ] Sección «Tiempo trabajado» en `ticket.html` / `ticket.js`
- [ ] Formulario (minutos, fecha, descripción) + lista + total
- [ ] Consumo de API con manejo de errores
- [ ] Visibilidad por rol (solicitante ve solo total)

---

## 🔗 Referencias

- **Propuesta completa:** [`Examen_Final/propuesta_time_entries.md`](Examen_Final/propuesta_time_entries.md)
- **Enunciado oficial:** [`Examen_Final/examen_final_programaci_n_ii_helpdesk_edu.md`](Examen_Final/examen_final_programaci_n_ii_helpdesk_edu.md)
- **Rúbrica Serie II:** [`Examen_Final/serie_ii_pr_ctica_sobre_helpdesk_edu.md`](Examen_Final/serie_ii_pr_ctica_sobre_helpdesk_edu.md)

---

## 🛠️ Ejecución local (cuando PostgreSQL esté disponible)

```bash
# Configurar base de pruebas
export TEST_DATABASE_URL="postgresql+psycopg://helpdesk:helpdesk@localhost:5433/helpdesk_test"

# Recrear esquema (una sola vez)
psql -U helpdesk -d helpdesk_test -f docs/database/database.sql
psql -U helpdesk -d helpdesk_test -f docs/database/functions_triggers.sql
psql -U helpdesk -d helpdesk_test -f docs/database/seed.sql

# Ejecutar pruebas de integración
uv run pytest tests/test_time_entries.py -m integration -v

# Ejecutar todas las pruebas (unitarias + integración)
uv run pytest -v
```

---

**Fecha de implementación:** 12 de noviembre de 2026  
**Tiempo invertido:** Fase 1 (entidad + persistencia): ~90 minutos
