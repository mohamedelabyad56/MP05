# Sistema de Reservas - Documentación

## Normas para actualizar UML
- Actualiza el diagrama UML antes de modificar el código.
- Usa PlantUML para consistencia.
- Exporta el diagrama como PNG y guárdalo en `diagrams/`.

## Buenas prácticas para commits
- Usa mensajes descriptivos: "Añadida clase Cliente al UML y código".
- Trabaja en ramas: `feature/nueva-funcionalidad`.
- Haz pull requests para revisión.

## Ciclo de trabajo
1. Diseña/actualiza el diagrama UML en `diagrams/`.
2. Implementa el código en `src/`.
3. Verifica la sincronización UML-código.
4. Commit y push en rama específica.

## Ejemplo
- Añadir clase `Cliente`:
  - Actualizar `diagrams/reservas.puml`.
  - Implementar `src/cliente.py`.
  - Commit: "Añadida clase Cliente al UML y código".