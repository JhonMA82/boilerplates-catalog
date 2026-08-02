# AGENTS.md

## Propósito

Este repositorio documenta decisiones. No contiene los boilerplates externos.

## Fuente de verdad

1. `catalog.json`
2. `README.md`
3. fichas en `docs/`
4. `CHANGELOG.md`

## Reglas para agentes

- No eliminar matices para acortar documentos.
- No promover una entrada sin piloto/evidencia.
- Diferenciar hechos oficiales de evaluación interna.
- No afirmar multi-tenancy, RBAC o producción si no están verificados.
- Mantener el mapa de cobertura.
- Actualizar enlaces relativos.
- Ejecutar `python scripts/validate_catalog.py`.
- Actualizar `CHANGELOG.md`.
- No agregar una licencia sin decisión explícita.
- Usar español claro y conservar nombres técnicos oficiales.

## Cambio de entrada

Actualizar simultáneamente:

- `catalog.json`;
- ficha;
- README generado;
- matriz/comparación afectada;
- coverage map si aparece una nueva decisión;
- changelog.
