# Propuesta de módulo: Registro de tiempo trabajado (Time Entries)

**Proyecto:** HelpDesk EDU · **Práctica:** Serie II · **Versión:** 2 (ajustada a la rúbrica)

> **Nota de verificación:** esta propuesta debe compararse con la **ficha del Anexo B** de la práctica. Si la ficha pide un campo, regla o código de error distinto, la ficha prevalece y esta propuesta se ajusta. Los nombres de roles, estados y rutas deben confirmarse contra el repositorio real.

---

## 1. Nombre y problema

**Módulo:** Registro de tiempo (Time Entries).

HelpDesk ya registra qué pasó con un ticket (historial y comentarios), pero no cuánto esfuerzo costó atenderlo. Por eso los supervisores no pueden medir la carga de trabajo de cada técnico ni el tiempo dedicado a cada categoría. Este módulo permite que el personal de soporte anote los minutos trabajados en cada ticket y que el supervisor consulte el total acumulado.

## 2. Entidad nueva: `TimeEntry` (tabla `time_entries`)

| Campo | Tipo | Regla |
| :--- | :--- | :--- |
| `id` | SERIAL (PK) | Lo asigna la base de datos |
| `ticket_id` | INTEGER (FK → `tickets.id`) | Obligatorio; `ON DELETE CASCADE` (se borra junto con el ticket) |
| `technician_id` | INTEGER (FK → `users.id`) | Obligatorio; **lo asigna el servidor a partir del usuario autenticado**, nunca viene en el cuerpo de la petición; solo personal de soporte |
| `minutes` | INTEGER | Obligatorio; entre 1 y 480; `CHECK` también en base de datos |
| `description` | VARCHAR(255) | Obligatorio; no vacío tras `strip()`; qué trabajo se hizo |
| `worked_on` | DATE | Obligatorio; no puede ser una fecha futura |
| `created_at` | TIMESTAMP | Fecha y hora actuales por defecto |

## 3. Relaciones

- Un ticket tiene muchos registros de tiempo; cada registro pertenece a un solo ticket.
- Un usuario de soporte tiene muchos registros; cada registro tiene un único técnico.

```
USERS   (1) ----< (N) TIME_ENTRIES   (technician_id)
TICKETS (1) ----< (N) TIME_ENTRIES   (ticket_id)
```

Sigue el mismo patrón que `Comment` (`ticket_id` + `author_id`): relaciones con `back_populates` en `Ticket` y `User`, y cascada al borrar el ticket.

## 4. Reglas de negocio (en el servicio)

| # | Regla | Resultado si se incumple |
| :-: | :--- | :--- |
| R1 | El actor debe estar autenticado | 401 |
| R2 | Solo personal de soporte (técnico, supervisor, administrador) registra tiempo | 403, sin cambios |
| R3 | El ticket debe existir | 404 |
| R4 | El ticket no puede estar cerrado ni cancelado | 409, sin cambios |
| R5 | `minutes` entre 1 y 480 | Error de validación, sin cambios |
| R6 | `description` no vacía, máximo 255 caracteres | Error de validación, sin cambios |
| R7 | `worked_on` no puede ser futura | Error de validación, sin cambios |
| R8 | `technician_id` = usuario autenticado | (no depende del cliente) |

Todas las validaciones ocurren **antes** de escribir. Si alguna falla, no se persiste nada.

*Decisión de diseño:* no se exige que el técnico sea el asignado al ticket (como en la propuesta original). Si el Anexo B lo exige, se agrega como regla adicional con 403.

*Opcional:* anotar el registro en el historial del ticket **solo** si el proyecto ya tiene un helper reutilizable; no es parte del mínimo evaluado.

## 5. API (todas bajo `/api`)

### `POST /api/tickets/{ticket_id}/time-entries`

Cuerpo:

```json
{ "minutes": 45, "description": "Cambio de tóner y limpieza de rodillo", "worked_on": "2026-11-12" }
```

Respuesta `201`:

```json
{ "id": 1, "ticket_id": 12, "technician_id": 7, "minutes": 45,
  "description": "Cambio de tóner y limpieza de rodillo",
  "worked_on": "2026-11-12", "created_at": "2026-11-12T20:03:00", "total_minutes": 45 }
```

### `GET /api/tickets/{ticket_id}/time-entries`

| Rol | Qué recibe |
| :--- | :--- |
| Técnico, supervisor, administrador | `{ ticket_id, total_minutes, entries: [ ... ] }` |
| Solicitante **dueño** del ticket | `{ ticket_id, total_minutes }` — sin `entries`, sin técnico ni descripciones |
| Solicitante de **otro** ticket | Denegado (403/404 según la convención del proyecto) |
| Sin autenticación | 401 |

Los permisos se aplican **en el servidor**; la pantalla solo los refleja.

## 6. Caso de uso

1. Ana (solicitante) crea el ticket #12, «La impresora no imprime» (Hardware, prioridad alta).
2. El supervisor se lo asigna a Luis y el ticket pasa a «en progreso».
3. Luis registra 45 minutos: «Cambio de tóner y limpieza de rodillo», con la fecha de hoy.
4. El sistema valida R1–R8 y guarda el registro.
5. Al día siguiente Luis registra 30 minutos más. El ticket muestra un total de 75 minutos.
6. Luis marca el ticket como resuelto; el supervisor consulta el tiempo total invertido.
7. Si Ana intenta registrar tiempo → 403. Si el ticket está cerrado → 409. En ambos casos no se crea ningún registro.

## 7. Pantalla (obligatoria)

Sección **«Tiempo trabajado»** integrada en la pantalla de detalle del ticket del cliente web existente.

- **Formulario** (técnico, supervisor, administrador): minutos (1–480), fecha (por defecto hoy, máximo hoy), descripción (máx. 255) y botón «Registrar tiempo».
- **Lista** de registros (fecha, técnico, minutos, descripción) y **total acumulado**.
- **Solicitante:** ve solo el total; sin formulario ni lista.
- **Consumo real de la API** con el mismo mecanismo de autenticación del resto del cliente.
- **Retroalimentación:** mensaje de éxito; mensaje de error con el detalle que devuelva la API (403, 409, validación).
- **Lectura al recargar:** el dato guardado sigue apareciendo después de recargar la página.

## 8. Pruebas automatizadas

Contra la base de **PRUEBAS** aislada. Sin modificar pruebas preexistentes.

| # | Prueba | Efecto verificado |
| :-: | :--- | :--- |
| T1 | Técnico registra 45 min en ticket abierto | 201; fila creada; **legible desde una sesión nueva** |
| T2 | Registros de 45 y 30 min | GET devuelve `total_minutes = 75` |
| T3 | Solicitante intenta registrar | 403; **conteo de filas sin cambio** |
| T4 | Ticket cerrado / cancelado | 409; conteo sin cambio |
| T5 | Minutos 0 y 481, fecha futura, descripción vacía | Error de validación; conteo sin cambio |
| T6 | Solicitante dueño consulta | Solo `total_minutes`, sin `entries` |
| T7 | Solicitante de otro ticket / sin autenticación | 403-404 / 401 |
| T8 | Ticket inexistente | 404 |

## 9. Alcance

**Dentro:** tabla, modelo, repositorio, servicio, endpoints, pantalla, pruebas, datos de ejemplo **solo en la base de pruebas**.

**Fuera:** reportes por técnico o categoría, editar o borrar registros, exportar datos.

## 10. Mapa contra la rúbrica (25 pts)

| Criterio | Pts | Cómo se cubre |
| :--- | :-: | :--- |
| Entidad y relación | 5 | Secciones 2 y 3: modelo, FKs a `tickets` y `users`, campos del tema |
| Persistencia | 5 | Tabla/ORM, repositorio (`create`, `list_by_ticket`, `total_minutes`), T1 con sesión nueva |
| Servicio y API | 5 | Reglas R1–R8, rutas bajo `/api`, validación de entrada, permisos por rol en servidor |
| Pantalla funcional | 5 | Sección 7: formulario, consumo real, mensajes, lectura al recargar |
| Pruebas | 4 | T1–T2 camino feliz; T3–T5 rechazo sin mutación |
| Entrega verificable | 1 | Rama, archivos, salida real de pruebas, evidencia de ejecución local |

## 11. Por confirmar antes de implementar

- [ ] Que este módulo coincida con el asignado en el **Anexo A** y con la ficha del **Anexo B**.
- [ ] Nombres exactos de roles y de estados de ticket (cerrado, cancelado) en el repositorio.
- [ ] Prefijo real de rutas (`/api`) y convención de códigos de error de validación.
- [ ] Cómo se crean las tablas (migraciones o `create_all`) y cómo se configura la base de pruebas.
- [ ] Si no hay servicio de base de datos disponible: documentar la comprobación pendiente, sin afirmar que persistió.
