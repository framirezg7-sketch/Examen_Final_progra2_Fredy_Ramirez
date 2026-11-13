"""Dataclass de dominio para un registro de tiempo trabajado en un ticket.

Sigue el mismo patrón que app/models/comments.py:
- id es None hasta que el repositorio persiste el objeto (la base asigna la PK).
- El campo technician_id proviene del actor autenticado; nunca del cuerpo HTTP.
- worked_on es un date (DATE en la base), no datetime.
"""

from dataclasses import dataclass, field
from datetime import date, datetime

from app.domain.clock import now


@dataclass
class TimeEntry:
    # None hasta que el repositorio guarda el objeto: la base asigna la llave.
    id: int | None = field(default=None, kw_only=True)
    ticket_id: int
    technician_id: int
    minutes: int
    description: str
    worked_on: date
    created_at: datetime = field(default_factory=now)
