---
name: github-readme
description: Escribe y mejora README de GitHub en español, con foco en boilerplates y starters públicos. Úsalo cuando el usuario pida crear, redactar, generar, mejorar, auditar o corregir el README de un repositorio, aunque no lo llame por su nombre (ej. "escribe la documentación del repo", "el readme está incompleto", "hazme el readme del proyecto", "documenta este boilerplate"). También cuando el README existente tenga secciones faltantes, comandos desactualizados o formato que no renderiza en GitHub.
---

# GitHub README en español

## Por qué existe este skill

Un README mal hecho daña la adopción de un boilerplate: promete capacidades que no existen, lista comandos que ya no funcionan o no renderiza en GitHub. Este skill produce README que dicen la verdad sobre el repo, muestran cómo empezar en 60 segundos y se mantienen al día con el código. El objetivo no es la longitud ni los adornos: es que un visitante entienda qué es, si le sirve y cómo lo usa sin adivinar nada.

## Principios que gobiernan todo el trabajo

- **Veracidad primero.** Solo afirmar lo que se puede verificar en el repositorio (manifiestos, código, docs, CI). Nunca inventar características, screenshots, badges ni URLs.
- **Sin inflar.** Sin lluvia de badges, sin emojis (salvo que el usuario los pida), sin secciones de relleno ni frases genéricas de marketing.
- **Español claro**, conservando los nombres técnicos oficiales (nombres de paquetes, comandos, términos del ecosistema).
- **Respetar el contexto del repo.** Leer AGENTS.md, convenciones existentes y el idioma de los docs antes de decidir el tono.
- **Cambios mínimos al mejorar.** No reescribir por reescribir: conservar lo válido y corregir lo roto.

## Workflow: redactar desde cero

### 1. Inspeccionar el repositorio antes de escribir nada

Nunca escribir un README sin mirar primero el código. Revisar, en orden:

- Manifiesto de dependencias (`package.json`, `Cargo.toml`, `pyproject.toml`, `go.mod`, etc.): stack, scripts, binarios, engines, campos de metadata.
- Estructura de directorios: qué apps, paquetes o componentes incluye el proyecto.
- `docs/`, `AGENTS.md`, `README` anterior, config de CI: contexto y afirmaciones ya existentes.
- Licencia (`LICENSE` o campo de licencia en el manifiesto): solo mencionarla si está verificada; si es ambigua, preguntar o omitir sin inventar.
- `git log`/tags (opcional): nociones de madurez y versión.

### 2. Identificar la audiencia

¿Quién usará este boilerplate? Un desarrollador con una necesidad concreta (una app móvil, un dashboard, un SaaS). El README debe responder: qué es, para qué sirve, para quién, qué stack usa, cómo empezar.

### 3. Escribir con la plantilla

Usar siempre esta estructura, omitiendo las secciones que no apliquen:

```
# <Nombre>

<Una línea: qué es (starter/boilerplate de X)>

<Descripción de 2-4 líneas: problema que resuelve y para quién>

## Stack / Tecnología
<tabla o lista breve, con nombres oficiales y versiones si son verificables>

## Requisitos previos
<herramientas e instalaciones necesarias>

## Instalación y uso rápido
<comandos reales, verificados contra los scripts del repo, en el orden real>

## Scripts principales
<qué hace cada comando útil del manifiesto>

## Estructura del proyecto
<árbol resumido con un comentario corto por directorio>

## Configuración
<variables de entorno o ajustes, solo si existen; sin inventar valores>

## Documentación
<enlaces a docs oficiales o a docs/ del repositorio>

## Licencia
<solo si está verificada; con enlace al archivo LICENSE>
```

No agregar secciones cosméticas (Contribución, FAQ, Screenshots, Changelog) salvo que tengan contenido real y verificable o que el usuario las pida explícitamente.

### 4. Verificar antes de terminar

- Cada comando listado existe en el manifiesto/scripts del repo.
- Cada archivo referenciado existe (rutas exactas, respetando mayúsculas).
- No hay afirmaciones sin soporte en el código.
- El Markdown renderiza en GitHub.

## Workflow: mejorar un README existente

1. Leer el README actual y compararlo con la plantilla.
2. Diagnosticar problemas concretos: secciones faltantes, comandos desactualizados o inexistentes, afirmaciones no verificadas, enlaces rotos, formato que no renderiza (p. ej. sangrado de 4 espacios que rompe listas y tablas, mezcla de estilos de encabezado).
3. Conservar el contenido válido y el tono del proyecto.
4. Aplicar los cambios mínimos que acerquen al estándar, explicando qué se corrigió y por qué.

## Reglas de formato para que renderice bien en GitHub

- Jerarquía de encabezados correcta (`#` título, `##` secciones, sin saltar niveles).
- Tablas bien formadas: fila de encabezado, línea separadora `|---|---|`, filas consistentes.
- Bloques de código con lenguaje declarado (```bash, ```ts) y precedidos de línea en blanco.
- Línea en blanco entre bloques de Markdown que GitHub junta (listas, tablas, bloques de código).
- Enlaces relativos con rutas reales del repo (`./docs/...`).
- Preferir Markdown puro sobre HTML cuando Markdown alcanza.
- Código de ejemplo verificable: debe ser el de los scripts reales, no inventado.

## Recordatorio final

El README es la primera impresión del boilerplate: que un visitante sepa en menos de un minuto qué es, si le sirve y cómo arrancar, sin que el repositorio tenga que defenderse luego de promesas que no cumplió.
