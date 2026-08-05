# Changelog

## [1.2.3] - 2026-08-05

### Corregido

- Se amplió el skill `github-readme` con los mecanismos oficiales de GitHub (badges shields.io, alerts, Mermaid, emojis, task lists) y el flujo de modificación correcta: leer antes de tocar, consultar antes de eliminar o reestructurar, actualizar documentos vinculados y ejecutar validaciones del repo.

## [1.2.2] - 2026-08-05

### Corregido

- Mejora visual de los documentos para GitHub: badges de CI, estrellas, último commit y versión del catálogo en el README; emojis en encabezados de sección; alerts `[!IMPORTANT]` y `[!NOTE]` en README y fichas; diagramas Mermaid en `catalog-map.md` y `decision-tree.md` (la pregunta final obligatoria pasó a un alert al inicio del árbol); checkboxes en las secciones de curación de las 12 fichas de boilerplates.

## [1.2.1] - 2026-08-05

### Corregido

- Se eliminó la columna `Procedencia` de la tabla del catálogo en el README. La procedencia es metadata del proceso de selección (sigue en `catalog.json` y en la tabla de cada ficha) y no aporta a la decisión de uso; la columna `Estado` se conserva como señal de gobernanza principal.

## [1.2.0] - 2026-08-05

### Agregado

- Se incorporó el skill de OpenCode `github-readme` en `.opencode/skills/github-readme/` para redactar y mejorar README de GitHub en español, con foco en boilerplates y starters públicos.
- Se actualizó el README con la sección de skills y la estructura del repositorio.

## [1.1.0] - 2026-08-05

### Agregado

- Se incorporó React Starter Kit (kriasoft) como opción full-stack TypeScript para SaaS comercial con despliegue en el edge de Cloudflare, propuesta por el usuario.
- Ficha completa en `docs/boilerplates/react-starter-kit.md`.
- Comparación directa con Open SaaS en `docs/comparisons/open-saas-vs-react-starter-kit.md`.
- Se actualizaron el mapa del catálogo, el árbol de decisión, el mapa de cobertura y el README.

## [1.0.1] - 2026-08-02

### Corregido

- Se corrigió el formato Markdown de las fichas en `docs/boilerplates/`: se eliminó la sangría superior de 4 espacios que mezclaba tablas, encabezados y listas y que impedía el renderizado correcto en GitHub.
- Se agregó una línea en blanco tras el bloque del catálogo en `README.md`.

## [1.0.0] - 2026-08-02

### Rehecho

- Repositorio reconstruido desde cero después de detectar que la primera síntesis omitía decisiones esenciales.
- Se incorporó el contexto sectorial completo.
- Se separaron boilerplates, starters internos y packs de infraestructura.
- Se añadió el razonamiento detallado de Next vs. TanStack.
- Se documentó SpeedPy Full/Lite y su diferencia con FastAPI.
- Se incluyeron Full Stack FastAPI Template y Open SaaS con fichas completas.
- Se preservó GoShip como candidato especializado con casos de turnos, SSE, PWA, notificaciones y webhooks.
- Se añadió AI Assistant Starter, Institutional Operations Starter y Python Service Starter.
- Se incorporaron plataformas complementarias.
- Se agregó mapa de cobertura de la conversación, gobernanza, forks, seguridad y versionado.
