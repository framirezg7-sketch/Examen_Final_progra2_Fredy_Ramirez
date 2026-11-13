# SERIE II · Práctica sobre HelpDesk EDU · 25 puntos

**Tiempo sugerido:** 90 minutos dentro de las 2 horas totales.

Su módulo aparece en el **Anexo A**; la ficha específica está en el **Anexo B**. Impleméntelo en su repositorio local existente, actualizado con el trabajo de la semana 17; **no reinicie el proyecto ni cree un módulo aislado.**

La ficha indica un flujo vertical mínimo del tema asignado: entidad relacionada con `Ticket` o `User`, persistencia real con SQLAlchemy usando la base de pruebas aislada, una regla de negocio, API con control de acceso, pantalla funcional conectada a la API y una prueba automatizada. Se evalúa el flujo completo observable, no cada función opcional de la propuesta original. La pantalla se exige a todos por igual, aunque una propuesta antigua la dejara fuera de su alcance inicial.

---

## Piezas y límites de la práctica

| Capa | Evidencia mínima observable |
| :--- | :--- |
| **Entidad / relación** | Entidad nueva vinculada a `Ticket` o `User` existente; identificador y campos necesarios para el caso de uso de su ficha. |
| **Persistencia** | Tabla y repositorio SQLAlchemy para crear y recuperar el registro. La operación persiste: al consultar en una sesión nueva el dato sigue presente. No se modifica una base de datos real del curso para probarlo. |
| **Servicio / API** | Regla principal de su ficha en el servicio; ruta(s) bajo `/api` con entrada validada, actor autenticado y permisos del servidor. No revelar datos privados a usuarios no autorizados. |
| **Pantalla** | Sección integrada en el cliente web existente; permite ejecutar la operación indicada, informa éxito/error y refleja el dato guardado al recargar. |
| **Pruebas** | Al menos una prueba automatizada del caso específico de la ficha, incluyendo el efecto observable y el rechazo sin cambio de estado cuando corresponda. |

> **Importante:** Trabaje con una base de **PRUEBAS aislada**. No ejecute migraciones ni pruebas que borren datos en la base habitual; si no dispone del servicio de base de datos, documente qué comprobación quedó pendiente en lugar de afirmar que persistió. Ejecute las pruebas del proyecto que estén disponibles sin modificar las preexistentes.

**Entrega:** Conserve el trabajo en su copia local y anote la rama, los archivos modificados y los resultados de las pruebas. Entregue la copia y evidencia de funcionamiento por el medio que indique el catedrático. No se exige acceso al repositorio central privado ni un Pull Request.

---

## Rúbrica común (25 puntos)

| Criterio | Puntos | Evidencia |
| :--- | :---: | :--- |
| **Entidad y relación** | 5 | Modelo coherente (2), vínculo con entidad existente (2), campos del tema (1). |
| **Persistencia** | 5 | Tabla/ORM (2), repositorio (2), lectura desde otra sesión de prueba (1). |
| **Servicio y API** | 5 | Regla y errores de dominio (2), ruta y entrada (1), permisos efectivos (2). |
| **Pantalla funcional** | 5 | Formulario/acción integrada (2), consumo real de API (2), retroalimentación y lectura al recargar (1). |
| **Pruebas** | 4 | Camino feliz con efecto observable (2), caso de rechazo sin mutación (2). |
| **Entrega verificable** | 1 | Rama/archivos/resultados y evidencia de la ejecución local (1). |
| **TOTAL** | **25** | |

---

## Datos de entrega

* **Mi módulo (Anexo A):** `____________________`
* **Mi rama local:** `________________________________________`
* **Pruebas ejecutadas y resultado:** `____________________________________________________`
* **Archivos entregados / evidencia:** `___________________________________________________`