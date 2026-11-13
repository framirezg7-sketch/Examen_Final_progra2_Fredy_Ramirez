# UNIVERSIDAD MARIANO GÁLVEZ DE GUATEMALA
**FACULTAD DE INGENIERÍA EN SISTEMAS DE INFORMACIÓN**

| Campo | Detalle | Campo | Detalle |
| :--- | :--- | :--- | :--- |
| **Carrera:** | Ingeniería en Sistemas de Información | **Código:** | 090 |
| **Asignatura:** | Programación II | **Código:** | 090017 |
| **Ciclo:** | 2026 | **VARIANTE:** | - |
| **Fecha:** | 12 de noviembre de 2026 | **CALIFICACIÓN:** | Absoluta: 100/35 \| Relativa: 35/100 |
| **Catedrático:** | ING. RICHARD ORTIZ SASVIN | **Semestre / Sección:** | 2do. / Sección: 3 |
| **Duración:** | 120 min | **Vo. Bo:** | - |

**Tipo de Examen:** `[ ]` PRIMER PARCIAL | `[ ]` SEGUNDO PARCIAL | `[ ]` EXTRAORDINARIO | `[X]` FINAL | `[ ]` RECUPERACIÓN

---

### Datos del Estudiante
* **Nombre:** `__________________________________________________`
* **Carné:** `_________________________`
* **Fecha:** `_________________________`

---

# EVALUACIÓN FINAL DE PROGRAMACIÓN II
## Semanas 13 a 17 · Python · Proyecto HelpDesk EDU

### Instrucciones generales
* **Valor total:** 35 puntos (Serie I: 10 puntos · Serie II: 25 puntos).
* **Duración total:** 120 minutos (2 horas).
* **Distribución sugerida:** Serie I, 20 minutos; Serie II, 90 minutos; cierre y entrega, 10 minutos. Puede iniciar por cualquiera de las series, pero debe entregar ambas.
* **Modalidad:** Trabajo individual. Utilice su copia local existente del repositorio `helpdesk` desarrollada durante el curso; extienda su código sin crear una aplicación independiente. El repositorio central ahora es privado: no se exige clonar, descargar, hacer push ni abrir un Pull Request hacia él.
* **Recursos:** Puede consultar su propio código y la documentación oficial. No comparta soluciones ni reciba ayuda de otras personas. El catedrático indicará al inicio si se permite usar herramientas de inteligencia artificial.

---

# SERIE I · Selección múltiple y verdadero o falso · 10 puntos

### Preguntas 1 a 10: Selección múltiple (5 puntos)
*0.5 puntos por respuesta correcta. Marque una sola letra; respuestas múltiples o en blanco reciben 0.*

#### Semana 13 · SQLAlchemy 2.x y patrón Repository

**1. Un servicio de tickets depende de un contrato Repository y no de SQLAlchemy directamente. ¿Cuál es la ventaja principal?**
* A. Permite cambiar o simular la persistencia sin modificar las reglas del servicio.
* B. Hace innecesarias las transacciones de la base de datos.
* C. Garantiza que todas las consultas sean más rápidas.
* D. Obliga al dominio a conocer las tablas y columnas.
* **Respuesta:** `______`

**2. Durante una transacción, `session.flush()` envía un `INSERT` y luego ocurre un error antes de `commit()`. ¿Qué debe suceder al ejecutar `rollback()`?**
* A. La fila queda confirmada porque flush equivale a commit.
* B. La fila se descarta porque flush no confirma la transacción.
* C. La fila se duplica en el siguiente commit.
* D. La sesión convierte automáticamente el error en una respuesta HTTP.
* **Respuesta:** `______`

#### Semana 14 · FastAPI, validación y API segura

**3. Una API recibe un cuerpo con un correo de formato inválido. ¿Qué responsabilidad cumple Pydantic en este límite del sistema?**
* A. Ejecutar consultas SQL concatenando los campos recibidos.
* B. Asignar permisos administrativos al usuario autenticado.
* C. Validar el contrato de entrada antes de ejecutar el caso de uso.
* D. Reemplazar todas las reglas de negocio del dominio.
* **Respuesta:** `______`

**4. ¿Cuál es la práctica correcta para almacenar contraseñas de usuarios?**
* A. Guardarlas en texto plano dentro de una tabla protegida.
* B. Cifrarlas con una clave incluida en el repositorio.
* C. Aplicar una sola vez un hash rápido sin sal.
* D. Guardar un hash adaptativo con sal, diseñado para contraseñas.
* **Respuesta:** `______`

#### Semana 15 · Patrones de diseño aplicados

**5. Varias rutas deben coordinar validación, persistencia y notificación en el mismo orden. ¿Qué aporta una Facade de casos de uso?**
* A. Una interfaz simple que coordina el subsistema sin exponer cada paso a la ruta.
* B. Una variable global compartida por todas las peticiones.
* C. Una sustitución completa de los repositorios.
* D. Una obligación de aplicar herencia entre rutas y servicios.
* **Respuesta:** `______`

**6. El sistema debe avisar a bitácora y correo cuando cambia el estado de un ticket, sin acoplar el servicio a receptores concretos. ¿Qué patrón encaja mejor?**
* A. Singleton, porque crea una única notificación global.
* B. Observer, porque suscriptores independientes reaccionan al evento.
* C. Repository, porque transforma eventos en filas.
* D. Facade, porque convierte cada receptor en una ruta HTTP.
* **Respuesta:** `______`

#### Semana 16 · Cliente web

**7. `fetch()` recibe una respuesta HTTP 422 de la API. ¿Qué debe hacer el cliente web?**
* A. Asumir que la promesa siempre se rechaza ante cualquier 4xx.
* B. Repetir la solicitud indefinidamente hasta obtener 200.
* C. Revisar `response.ok`, interpretar el cuerpo y mostrar retroalimentación útil.
* D. Acceder directamente a la base de datos para corregir el registro.
* **Respuesta:** `______`

**8. ¿Qué diseño mejora a la vez la accesibilidad y la adaptación del formulario a distintos tamaños de pantalla?**
* A. Usar solo colores para identificar errores y anchos fijos.
* B. Eliminar etiquetas para reducir el contenido visual.
* C. Mostrar todos los mensajes únicamente en la consola del navegador.
* D. Asociar etiquetas a campos, anunciar errores y usar una distribución responsiva.
* **Respuesta:** `______`

#### Semana 17 · Integración, pruebas y despliegue

**9. Una prueba crea un servicio con un repositorio en memoria y un notificador falso, sin API ni base real. ¿Cómo se clasifica?**
* A. Como prueba unitaria, porque aísla una unidad mediante dobles de prueba.
* B. Como prueba de despliegue, porque ejecuta código Python.
* C. Como prueba de interfaz, porque el servicio podría ser llamado por una pantalla.
* D. Como prueba de migración, porque usa objetos persistibles.
* **Respuesta:** `______`

**10. En Docker Compose, la aplicación debe conectarse al servicio llamado `db`. ¿Qué host y puerto debe usar desde su contenedor?**
* A. `localhost` y el puerto publicado en la computadora anfitriona.
* B. `db` y el puerto interno del servicio de base de datos.
* C. La dirección IP pública del equipo y el puerto de la API.
* D. Cualquier host, porque Compose redirige automáticamente localhost.
* **Respuesta:** `______`

---

### Preguntas 11 a 15: Verdadero o falso (5 puntos)
*1.0 punto por respuesta correcta. Justifique brevemente cada respuesta falsa; sin justificación, la respuesta falsa no obtiene el punto.*

**11. [13] Un Repository debe ejecutar commit después de cada operación para que el servicio no participe en la unidad de trabajo.**
* **Respuesta ($V/F$):** `______`
* **Si es falsa, justificación:** `____________________________________________________________`

**12. [14] Usar un ORM y consultas parametrizadas reduce el riesgo de inyección SQL, pero no reemplaza la validación ni el control de permisos.**
* **Respuesta ($V/F$):** `______`
* **Si es falsa, justificación:** `____________________________________________________________`

**13. [15] Singleton es la opción predeterminada para compartir servicios porque el estado global siempre facilita las pruebas.**
* **Respuesta ($V/F$):** `______`
* **Si es falsa, justificación:** `____________________________________________________________`

**14. [16] Un cliente web debe consumir la API y no conectarse directamente a la base de datos.**
* **Respuesta ($V/F$):** `______`
* **Si es falsa, justificación:** `____________________________________________________________`

**15. [17] Si cliente y API tienen orígenes distintos, basta con desactivar CORS en el navegador de cada usuario.**
* **Respuesta ($V/F$):** `______`
* **Si es falsa, justificación:** `____________________________________________________________`

---

# SERIE II · Práctica sobre HelpDesk EDU · 25 puntos

**Tiempo sugerido:** 90 minutos dentro de las 2 horas totales.

Su módulo aparece en el **Anexo A**; la ficha específica está en el **Anexo B**. Impleméntelo en su repositorio local existente, actualizado con el trabajo de la semana 17; **no reinicie el proyecto ni cree un módulo aislado.**

La ficha indica un flujo vertical mínimo del tema asignado: entidad relacionada con `Ticket` o `User`, persistencia real con SQLAlchemy usando la base de pruebas aislada, una regla de negocio, API con control de acceso, pantalla funcional conectada a la API y una prueba automatizada. Se evalúa el flujo completo observable, no cada función opcional de la propuesta original. La pantalla se exige a todos por igual, aunque una propuesta antigua la dejara fuera de su alcance inicial.

### Piezas y límites de la práctica

| Capa | Evidencia mínima observable |
| :--- | :--- |
| **Entidad / relación** | Entidad nueva vinculada a `Ticket` o `User` existente; identificador y campos necesarios para el caso de uso de su ficha. |
| **Persistencia** | Tabla y repositorio SQLAlchemy para crear y recuperar el registro. La operación persiste: al consultar en una sesión nueva el dato sigue presente. No se modifica una base de datos real del curso para probarlo. |
| **Servicio / API** | Regla principal de su ficha en el servicio; ruta(s) bajo `/api` con entrada validada, actor autenticado y permisos del servidor. No revelar datos privados a usuarios no autorizados. |
| **Pantalla** | Sección integrada en el cliente web existente; permite ejecutar la operación indicada, informa éxito/error y refleja el dato guardado al recargar. |
| **Pruebas** | Al menos una prueba automatizada del caso específico de la ficha, incluyendo el efecto observable y el rechazo sin cambio de estado cuando corresponda. |

> **Importante:** Trabaje con una base de **PRUEBAS aislada**. No ejecute migraciones ni pruebas que borren datos en la base habitual; si no dispone del servicio de base de datos, documente qué comprobación quedó pendiente en lugar de afirmar que persistió. Ejecute las pruebas del proyecto que estén disponibles sin modificar las preexistentes.

**Entrega:** Conserve el trabajo en su copia local y anote la rama, los archivos modificados y los resultados de las pruebas. Entregue la copia y evidencia de funcionamiento por el medio que indique el catedrático. No se exige acceso al repositorio central privado ni un Pull Request.

### Rúbrica común (25 puntos)

| Criterio | Puntos | Evidencia |
| :--- | :---: | :--- |
| **Entidad y relación** | 5 | Modelo coherente (2), vínculo con entidad existente (2), campos del tema (1). |
| **Persistencia** | 5 | Tabla/ORM (2), repositorio (2), lectura desde otra sesión de prueba (1). |
| **Servicio y API** | 5 | Regla y errores de dominio (2), ruta y entrada (1), permisos efectivos (2). |
| **Pantalla funcional** | 5 | Formulario/acción integrada (2), consumo real de API (2), retroalimentación y lectura al recargar (1). |
| **Pruebas** | 4 | Camino feliz con efecto observable (2), caso de rechazo sin mutación (2). |
| **Entrega verificable** | 1 | Rama/archivos/resultados y evidencia de la ejecución local (1). |
| **TOTAL** | **25** | |

### Registro de entrega
* **Mi módulo (Anexo A):** `____________________`
* **Mi rama local:** `________________________________________`
* **Pruebas ejecutadas y resultado:** `____________________________________________________`
* **Archivos entregados / evidencia:** `___________________________________________________`

---

# ANEXO A · Módulos asignados a los 27 estudiantes habilitados

Busque su nombre y número de ficha. «Propuesta» conserva el tema entregado; «Docente» es un módulo nuevo asignado a quien no entregó propuesta. No intercambie fichas con otro alumno.

| N. | Estudiante | Carné | Origen | Tema de la ficha |
| :---: | :--- | :--- | :--- | :--- |
| **1** | ACABAL HERNANDEZ, SINDI CARINA | 21-6522 | Propuesta | Registro de tiempo con nota obligatoria |
| **2** | ALVARADO PALOMINO, PABLO JOSUE | 20-14490 | Propuesta | Canal de recepción del reporte |
| **3** | BARRIOS LEMUS, ESDRASS JAZIRY D JORKAEFF | 25-6910 | Docente | Inventario de activos atendidos |
| **4** | CALDERON MAZARIEGOS, ANYELO GERARDO | 24-7528 | Propuesta | Nota privada de coordinación |
| **5** | CARCAMO MIRANDA, HERBERT DANIEL | 23-13916 | Docente | Agenda de visitas técnicas |
| **6** | CETINO RIOS, JESSER LICINIO | 24-13995 | Propuesta | Lista de tareas de resolución |
| **7** | COLON SALGUERO, KRISTA | 25-17466 | Propuesta | Incidente masivo con vinculación controlada |
| **8** | CORTEZ RAMIREZ, GENCER URIEL | 22-10331 | Docente | Préstamo temporal de equipo |
| **9** | CUJCUJ CONTRERAS, CRISTOPHER ALEXANDER | 24-11483 | Docente | Etiquetas operativas del caso |
| **10** | DUEÑAS INTERIANO, JOSELINE NOEMY | 24-8611 | Propuesta | Avance con estado resultante |
| **11** | Duque, Peter | 18-2312 | Docente | Artículos breves de conocimiento |
| **12** | ESCOBAR MELETZ, JOSÉ JAVIER | 23-5367 | Docente | Escalación con motivo y nivel |
| **13** | FLORES TUNCHE, LUIS DANIEL | 19-10697 | Docente | Turnos de guardia de soporte |
| **14** | GALINDO PEREZ, PABLO MOISES | 23-8697 | Propuesta | Nota de seguimiento con visibilidad |
| **15** | GAMEZ MEDINA, OSVIN LEONEL | 24-7005 | Propuesta | Bitácora interna cronológica |
| **16** | JEREZ ALVAREZ, HENRY EDUARDO | 23-21006 | Docente | Ubicaciones físicas de atención |
| **17** | LOPEZ PELICO, DELMI ANDREA | 24-21030 | Propuesta | Seguimiento de intentos de solución |
| **18** | MAYEN FAJARDO, MAYNOR ALESSANDRO | 22-8594 | Docente | Gestión de proveedores externos |
| **19** | MAZATE YOQUE, MAYCO DANIEL | 18-4681 | Propuesta | Solución reutilizable de ticket cerrado |
| **20** | MORALES UPUN, JOSE LUIS | 24-15706 | Propuesta | Feedback CSAT del solicitante |
| **21** | RAMIREZ GOMEZ, FREDY ALEXANDER | 23-15803 | Propuesta | Tiempo trabajado con fecha válida |
| **22** | RECINOS MOTA, JOSE ANTONIO | 25-5657 | Propuesta | Encuesta única al resolver |
| **23** | SABAN CUA, JONATHAN JOSUE | 23-18023 | Propuesta | Contactos alternos del caso |
| **24** | SIERRA LIMATUJ, JAVIER ARMANDO | 24-1252 | Propuesta | Tiempo de trabajo del técnico asignado |
| **25** | SOLIS YOCUTE, PRINCE ESTUARDO | 17-1035 | Propuesta | Nota de relevo entre técnicos |
| **26** | TUBAC COJ, JUAN CARLOS | 19-2413 | Propuesta | Valoración posterior al cierre |
| **27** | VASQUEZ MÉNDEZ, MERCEDES MARÍA JOSE | 24-6568 | Propuesta | Historial justificado de reasignación |

---

# ANEXO B · Fichas individuales del módulo

Cada ficha define el flujo mínimo evaluable del tema asignado en 90 minutos sugeridos. Los detalles restantes de la propuesta original no son obligatorios para obtener los 25 puntos.

### Ficha 01 · ACABAL HERNANDEZ, SINDI CARINA · Registro de tiempo con nota obligatoria *(propuesta)*
* **Entidad y relación:** `WorkLog` pertenece a `Ticket` y a `User` autor; un ticket acumula muchos registros.
* **Regla principal:** Solo personal registra entre 1 y 1440 minutos en tickets abiertos o en progreso, con nota no vacía.
* **Operación demostrable:** Registrar un período y mostrar el total acumulado del ticket.
* **API y rol:** `POST /api/tickets/{ticket_id}/work-logs` · técnico, supervisor o administrador.
* **Pantalla:** En el detalle, el personal ve minutos, nota, botón *Registrar* y la lista con total; el solicitante no ve la sección.
* **Prueba enfocada:** Un registro válido aumenta el total; 0 minutos se rechaza sin crear el registro.

### Ficha 02 · ALVARADO PALOMINO, PABLO JOSUÉ · Canal de recepción del reporte *(propuesta)*
* **Entidad y relación:** `ReporteCanal` pertenece uno a uno a `Ticket` y puede referenciar un ticket anterior.
* **Regla principal:** Cada ticket tiene un solo canal y los canales `Meet` exigen fecha de reunión.
* **Operación demostrable:** Guardar el canal de un ticket y consultarlo desde su detalle.
* **API y rol:** `POST /api/tickets/{ticket_id}/report-channel` · personal autorizado.
* **Pantalla:** Un selector cambia la visibilidad de la fecha para *Meet* y *Guardar* muestra el canal registrado.
* **Prueba enfocada:** *Meet* sin fecha se rechaza; *WhatsApp* sin fecha se guarda para el ticket correcto.

### Ficha 03 · BARRIOS LEMUS, ESDRASS JAZIRY D JORKAEFF · Inventario de activos atendidos *(docente)*
* **Entidad y relación:** `ActivoAtendido` pertenece a `Ticket` y conserva código y descripción del equipo asociado.
* **Regla principal:** Solo personal registra un código de activo no vacío y no lo repite dentro del mismo ticket.
* **Operación demostrable:** Registrar el activo atendido directamente en el ticket.
* **API y rol:** `POST /api/tickets/{ticket_id}/assets` · técnico, supervisor o administrador.
* **Pantalla:** El detalle del ticket recibe código y descripción y muestra los activos atendidos al recargar.
* **Prueba enfocada:** Un código duplicado en el mismo ticket se rechaza sin añadir otra asociación.

### Ficha 04 · CALDERON MAZARIEGOS, ANYELO GERARDO · Nota privada de coordinación *(propuesta)*
* **Entidad y relación:** `InternalNote` pertenece a `Ticket` y tiene un `User` autor; un ticket tiene muchas notas.
* **Regla principal:** Solo el personal agrega texto no vacío y ninguna nota privada se entrega al solicitante.
* **Operación demostrable:** Agregar una nota y listar el historial privado del ticket.
* **API y rol:** `POST /api/tickets/{ticket_id}/internal-notes` · técnico o supervisor.
* **Pantalla:** El detalle del personal separa *Notas internas* de comentarios y muestra autor y fecha; para solicitantes la sección no existe.
* **Prueba enfocada:** Una nota creada por técnico aparece al personal y queda ausente en la respuesta del solicitante.

### Ficha 05 · CÁRCAMO MIRANDA, HERBERT DANIEL · Agenda de visitas técnicas *(docente)*
* **Entidad y relación:** `VisitaTecnica` pertenece a `Ticket` y `User` técnico, con fecha programada y ubicación.
* **Regla principal:** La visita debe ser futura y solo se agenda para un ticket abierto con técnico asignado.
* **Operación demostrable:** Programar una visita y verla en la agenda.
* **API y rol:** `POST /api/tickets/{ticket_id}/visits` · supervisor o técnico asignado.
* **Pantalla:** El ticket ofrece fecha, hora y ubicación; *Guardar* agrega la visita a una lista de próximas visitas.
* **Prueba enfocada:** Una fecha pasada se rechaza y no aparece en la agenda.

### Ficha 06 · CETINO RIOS, JESSER LICINIO · Lista de tareas de resolución *(propuesta)*
* **Entidad y relación:** `TareaTicket` pertenece a `Ticket`; un ticket contiene muchas tareas pendientes o completadas.
* **Regla principal:** Solo el técnico asignado administra tareas; el solicitante únicamente consulta el progreso.
* **Operación demostrable:** Agregar una tarea y marcarla como completada.
* **API y rol:** `POST /api/tickets/{ticket_id}/tasks` · técnico asignado.
* **Pantalla:** En el detalle se agrega una descripción y la lista permite marcar una tarea; el solicitante la ve sin controles de edición.
* **Prueba enfocada:** Completar una tarea del ticket cambia solo esa tarea de pendiente a completada.

### Ficha 07 · COLON SALGUERO, KRISTA · Incidente masivo con vinculación controlada *(propuesta)*
* **Entidad y relación:** `Incident` agrupa muchos `Ticket`; cada ticket pertenece como máximo a un incidente.
* **Regla principal:** Solo supervisor o administrador vincula un ticket abierto a un incidente todavía abierto.
* **Operación demostrable:** Crear un incidente y vincularle un ticket elegible.
* **API y rol:** `POST /api/incidents/{incident_id}/tickets` · supervisor o administrador.
* **Pantalla:** La pantalla *Incidentes* crea el registro y su detalle permite ingresar un número de ticket y ver los vinculados.
* **Prueba enfocada:** Un ticket ya vinculado no puede agregarse a un segundo incidente y permanece en el primero.

### Ficha 08 · CORTEZ RAMIREZ, GENCER URIEL · Préstamo temporal de equipo *(docente)*
* **Entidad y relación:** `PrestamoEquipo` pertenece a `Ticket` y guarda etiqueta del equipo, receptor y devolución esperada; no requiere un inventario adicional.
* **Regla principal:** Solo personal registra etiqueta y fecha futura; un mismo ticket no admite dos préstamos activos con esa etiqueta.
* **Operación demostrable:** Crear un préstamo de equipo asociado directamente al ticket.
* **API y rol:** `POST /api/tickets/{ticket_id}/equipment-loans` · técnico o supervisor.
* **Pantalla:** El detalle captura etiqueta del equipo, receptor y fecha; al guardar muestra el préstamo activo al recargar.
* **Prueba enfocada:** Un segundo préstamo activo con igual etiqueta y ticket se rechaza sin crear registro.

### Ficha 09 · CUJCUJ CONTRERAS, CRISTOPHER ALEXANDER · Etiquetas operativas del caso *(docente)*
* **Entidad y relación:** `EtiquetaTicket` pertenece a `Ticket` y guarda el texto de una etiqueta operativa; no requiere un catálogo adicional.
* **Regla principal:** Solo personal agrega un texto no vacío y no duplica la misma etiqueta en un ticket.
* **Operación demostrable:** Agregar una etiqueta y mostrarla en el detalle del ticket.
* **API y rol:** `POST /api/tickets/{ticket_id}/tags` · personal de soporte.
* **Pantalla:** El detalle permite ingresar la etiqueta y muestra las etiquetas guardadas como chips al recargar.
* **Prueba enfocada:** Agregar dos veces la misma etiqueta conserva un solo registro.

### Ficha 10 · DUEÑAS INTERIANO, JOSELINE NOEMY · Avance con estado resultante *(propuesta)*
* **Entidad y relación:** `SeguimientoTicket` pertenece a `Ticket` y a `User`; conserva descripción, fecha y estado resultante.
* **Regla principal:** Técnicos y administradores registran una descripción no vacía con un estado permitido.
* **Operación demostrable:** Guardar un avance y consultar la secuencia cronológica.
* **API y rol:** `POST /api/tickets/{ticket_id}/tracking` · técnico o administrador.
* **Pantalla:** El detalle ofrece descripción y estado; al guardar agrega una fila con responsable y fecha al historial.
* **Prueba enfocada:** Un avance válido queda asociado al ticket y un estado desconocido se rechaza.

### Ficha 11 · Duque, Peter · Artículos breves de conocimiento *(docente)*
* **Entidad y relación:** `ArticuloConocimiento` puede referenciar un `Ticket` resuelto como origen.
* **Regla principal:** Solo personal publica título y solución no vacíos desde un ticket resuelto.
* **Operación demostrable:** Publicar un artículo y encontrarlo por título.
* **API y rol:** `POST /api/knowledge-articles` · técnico, supervisor o administrador.
* **Pantalla:** Desde un ticket resuelto se abre un formulario; la pantalla *Conocimiento* busca y muestra título y solución.
* **Prueba enfocada:** Un ticket abierto no permite publicar y la búsqueda no devuelve artículo nuevo.

### Ficha 12 · ESCOBAR MELÉTZ, JOSÉ JAVIER · Escalación con motivo y nivel *(docente)*
* **Entidad y relación:** `Escalacion` pertenece a `Ticket` y registra nivel, motivo y autor.
* **Regla principal:** Solo personal escala un ticket activo a un nivel mayor que el actual con motivo obligatorio.
* **Operación demostrable:** Escalar un ticket un nivel y reflejarlo en su detalle.
* **API y rol:** `POST /api/tickets/{ticket_id}/escalations` · técnico o supervisor.
* **Pantalla:** El detalle muestra nivel actual, selector de nivel superior y motivo; confirmar actualiza la insignia y el historial.
* **Prueba enfocada:** Intentar el mismo nivel se rechaza sin añadir historial ni cambiar la insignia.

### Ficha 13 · FLORES TUNCHE, LUIS DANIEL · Turnos de guardia de soporte *(docente)*
* **Entidad y relación:** `TurnoGuardia` pertenece a `User` técnico e incluye inicio y fin.
* **Regla principal:** El supervisor crea turnos con fin posterior al inicio y sin traslape para el mismo técnico.
* **Operación demostrable:** Asignar un turno y mostrarlo en el calendario diario.
* **API y rol:** `POST /api/on-call-shifts` · supervisor o administrador.
* **Pantalla:** La pantalla *Turnos* captura técnico, inicio y fin; al guardar agrega una franja al calendario.
* **Prueba enfocada:** Un turno traslapado se rechaza y el calendario conserva solo el turno original.

### Ficha 14 · GALINDO PÉREZ, PABLO MOISES · Nota de seguimiento con visibilidad *(propuesta)*
* **Entidad y relación:** `TicketNote` pertenece a `Ticket` y `User`, con indicador `es_interno`.
* **Regla principal:** El personal puede marcar una nota interna; el solicitante solo recibe notas públicas.
* **Operación demostrable:** Crear una nota interna y comprobar el listado filtrado por rol.
* **API y rol:** `POST /api/tickets/{ticket_id}/notes` · técnico; `GET` · participante del ticket.
* **Pantalla:** El personal ve texto, casilla *Nota interna* y todas las tarjetas; el solicitante ve únicamente las públicas.
* **Prueba enfocada:** La consulta del solicitante omite la nota marcada interna sin borrar el registro.

### Ficha 15 · GÁMEZ MEDINA, OSVIN LEONEL · Bitácora interna cronológica *(propuesta)*
* **Entidad y relación:** `NotaInterna` pertenece a `Ticket`; varias notas forman una bitácora ordenada.
* **Regla principal:** Solo técnico o administrador agrega contenido no vacío y el orden visible es cronológico.
* **Operación demostrable:** Agregar un diagnóstico y recuperar la bitácora ordenada.
* **API y rol:** `POST /api/tickets/{ticket_id}/private-log` · técnico o administrador.
* **Pantalla:** Una caja de texto y *Agregar nota* actualizan el historial cronológico privado con autor y fecha.
* **Prueba enfocada:** Dos notas creadas en distinto momento se listan en el mismo orden en que fueron registradas.

### Ficha 16 · JEREZ ALVAREZ, HENRY EDUARDO · Ubicaciones físicas de atención *(docente)*
* **Entidad y relación:** `UbicacionAtencion` pertenece a `Ticket` y registra edificio y área donde se atenderá el caso.
* **Regla principal:** Solo personal registra edificio y área no vacíos para un ticket existente.
* **Operación demostrable:** Registrar una ubicación física directamente en el ticket.
* **API y rol:** `POST /api/tickets/{ticket_id}/service-locations` · técnico o supervisor.
* **Pantalla:** El detalle del ticket recibe edificio y área y muestra la ubicación guardada al recargar.
* **Prueba enfocada:** Un área vacía se rechaza sin cambiar la ubicación del ticket.

### Ficha 17 · LÓPEZ PELICÓ, DELMI ANDREA · Seguimiento de intentos de solución *(propuesta)*
* **Entidad y relación:** `SeguimientoSolucion` pertenece a `Ticket` y a `User` técnico, con acción y resultado.
* **Regla principal:** La acción y el resultado son obligatorios y registrar un intento no cambia automáticamente el estado del ticket.
* **Operación demostrable:** Registrar un intento y consultar los intentos previos.
* **API y rol:** `POST /api/tickets/{ticket_id}/solution-attempts` · técnico.
* **Pantalla:** El detalle muestra acción, resultado, botón *Guardar* y una lista de intentos anteriores.
* **Prueba enfocada:** Guardar un intento conserva el estado actual del ticket y añade acción y resultado al historial.

### Ficha 18 · MAYEN FAJARDO, MAYNOR ALESSANDRO · Gestión de proveedores externos *(docente)*
* **Entidad y relación:** `IntervencionProveedor` pertenece a `Ticket` y guarda nombre de proveedor y número de caso externo, sin catálogo nuevo.
* **Regla principal:** Solo personal registra proveedor y número de caso no vacíos para un ticket existente.
* **Operación demostrable:** Registrar la intervención externa y mostrar su número de caso.
* **API y rol:** `POST /api/tickets/{ticket_id}/vendor-interventions` · supervisor o administrador.
* **Pantalla:** El ticket captura proveedor y número externo; al guardar muestra el caso y la fecha al recargar.
* **Prueba enfocada:** Un número de caso vacío se rechaza sin crear la intervención.

### Ficha 19 · MAZATE YOQUE, MAYCO DANIEL · Solución reutilizable de ticket cerrado *(propuesta)*
* **Entidad y relación:** `Solucion` pertenece a `Ticket` cerrado; un ticket puede documentar varias soluciones.
* **Regla principal:** Solo se registra título y descripción no vacíos para un ticket cerrado.
* **Operación demostrable:** Registrar una solución y encontrarla por una parte de su título.
* **API y rol:** `POST /api/solutions` · técnico; `GET /api/solutions?query=` · personal.
* **Pantalla:** Un formulario guarda ticket, título y solución; el buscador presenta coincidencias con fecha y ticket.
* **Prueba enfocada:** Un ticket abierto rechaza la solución sin persistirla; uno cerrado permite buscarla después.

### Ficha 20 · MORALES UPUN, JOSE LUIS · Feedback CSAT del solicitante *(propuesta)*
* **Entidad y relación:** `TicketFeedback` pertenece uno a uno a `Ticket` y almacena puntuación y comentario.
* **Regla principal:** Solo el solicitante califica una vez su ticket cerrado con valor de 1 a 5.
* **Operación demostrable:** Enviar la calificación y mostrar la confirmación.
* **API y rol:** `POST /api/tickets/{ticket_id}/feedback` · solicitante propietario.
* **Pantalla:** Al cerrar el ticket aparece un selector de 1 a 5, comentario opcional y *Registrar feedback*; después queda en modo lectura.
* **Prueba enfocada:** El segundo envío para el mismo ticket se rechaza y conserva la primera calificación.

### Ficha 21 · RAMÍREZ GÓMEZ, FREDY ALEXANDER · Tiempo trabajado con fecha válida *(propuesta)*
* **Entidad y relación:** `TimeEntry` pertenece a `Ticket` y `User` técnico, con minutos, descripción y fecha trabajada.
* **Regla principal:** Personal registra de 1 a 480 minutos, descripción obligatoria y fecha no futura en ticket no cerrado ni cancelado.
* **Operación demostrable:** Registrar tiempo y recalcular el total del ticket.
* **API y rol:** `POST /api/tickets/{ticket_id}/time-entries` · personal de soporte.
* **Pantalla:** La sección muestra minutos, fecha, descripción, lista y total; el solicitante ve solo el total.
* **Prueba enfocada:** Una fecha futura se rechaza sin cambiar la lista ni el total acumulado.

### Ficha 22 · RECINOS MOTA, JOSÉ ANTONIO · Encuesta única al resolver *(propuesta)*
* **Entidad y relación:** `EncuestaSatisfaccion` pertenece como máximo una vez a `Ticket`.
* **Regla principal:** Un ticket resuelto admite una sola calificación de 1 a 5 y comentario opcional.
* **Operación demostrable:** Enviar una encuesta y consultarla desde el ticket.
* **API y rol:** `POST /api/tickets/{ticket_id}/satisfaction-survey` · solicitante.
* **Pantalla:** El ticket resuelto muestra pregunta, opciones 1 a 5, comentario y *Enviar encuesta*; luego muestra la respuesta guardada.
* **Prueba enfocada:** Un ticket todavía abierto rechaza la encuesta y no crea ningún registro.

### Ficha 23 · SABÁN CÚA, JONATHAN JOSUÉ · Contactos alternos del caso *(propuesta)*
* **Entidad y relación:** `ContactoAlterno` pertenece a `Ticket` y registra quién lo agregó, sin crear un `User`.
* **Regla principal:** Solo solicitante propietario o personal agrega nombre, teléfono válido, relación permitida y motivo a un ticket abierto.
* **Operación demostrable:** Agregar un contacto y listarlo en el detalle.
* **API y rol:** `POST /api/tickets/{ticket_id}/alternate-contacts` · propietario o personal.
* **Pantalla:** La sección muestra formulario y lista con nombre, teléfono, relación, motivo y fecha a los participantes autorizados.
* **Prueba enfocada:** Un teléfono con menos de ocho dígitos se rechaza y la lista permanece sin cambios.

### Ficha 24 · SIERRA LIMATUJ, JAVIER ARMANDO · Tiempo de trabajo del técnico asignado *(propuesta)*
* **Entidad y relación:** `WorkLog` pertenece a `Ticket` y `User` técnico; varios registros producen un total.
* **Regla principal:** El técnico registra minutos positivos solo en un ticket que tiene asignado y está en progreso.
* **Operación demostrable:** Agregar un registro y actualizar el total visible al personal.
* **API y rol:** `POST /api/tickets/{ticket_id}/worklogs` · técnico asignado.
* **Pantalla:** El personal ve fecha, minutos y nota dentro del ticket; el solicitante no ve datos internos de esfuerzo.
* **Prueba enfocada:** Un técnico no asignado recibe rechazo y no altera el total del ticket.

### Ficha 25 · SOLIS YOCUTÉ, PRINCE ESTUARDO · Nota de relevo entre técnicos *(propuesta)*
* **Entidad y relación:** `NotaInterna` pertenece a `Ticket` y `User` autor; funciona como relevo privado de soporte.
* **Regla principal:** Solo personal agrega notas a tickets en atención y el solicitante nunca recibe su contenido.
* **Operación demostrable:** Dejar una nota de relevo y verla con otra cuenta técnica.
* **API y rol:** `POST /api/tickets/{ticket_id}/handover-notes` · personal técnico.
* **Pantalla:** En el detalle del personal, *Agregar nota interna* actualiza una bitácora; la vista del solicitante no muestra la sección.
* **Prueba enfocada:** Una nota creada por un técnico es visible para otro técnico y no para el solicitante.

### Ficha 26 · TUBAC COJ, JUAN CARLOS · Valoración posterior al cierre *(propuesta)*
* **Entidad y relación:** `Satisfaction` pertenece uno a uno a `Ticket`, con valoración, comentario y fecha.
* **Regla principal:** El solicitante puede valorar una sola vez un ticket resuelto con una puntuación dentro del rango permitido.
* **Operación demostrable:** Guardar la valoración y consultarla junto con el ticket.
* **API y rol:** `POST /api/tickets/{ticket_id}/satisfaction` · solicitante propietario.
* **Pantalla:** La pantalla identifica el ticket, permite elegir valoración y comentario, y reemplaza *Guardar* por el resumen enviado.
* **Prueba enfocada:** Una puntuación fuera del rango se rechaza sin ocupar la evaluación única del ticket.

### Ficha 27 · VÁSQUEZ MÉNDEZ, MERCEDES MARÍA JOSÉ · Historial justificado de reasignación *(propuesta)*
* **Entidad y relación:** `ReasignacionTicket` pertenece a `Ticket` y referencia técnico anterior y nuevo.
* **Regla principal:** Supervisor o administrador reasigna un ticket activo a un técnico diferente con motivo obligatorio.
* **Operación demostrable:** Reasignar el ticket y mostrar el cambio en su historial.
* **API y rol:** `POST /api/tickets/{ticket_id}/reassignments` · supervisor o administrador.
* **Pantalla:** Un panel selecciona nuevo técnico, exige motivo y al confirmar actualiza responsable e historial de traspasos.
* **Prueba enfocada:** Reasignar crea el historial y cambia el responsable; un motivo vacío no modifica ninguno.