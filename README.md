# Blog de robótica

## Descripción general

Este proyecto consiste en un blog de robótica orientado a la lectura, diseñado para ser sencillo, claro y adaptable tanto a móviles como a ordenadores. El objetivo principal es permitir que los visitantes descubran artículos recientes, lean contenidos completos y conozcan al autor a través de una sección de presentación.

La solución se plantea como un sitio en Django con una estructura de contenido gestionada desde el panel administrativo, sin necesidad de modificar plantillas para actualizar el contenido.

## Objetivo del producto

Crear un blog de autor en español que presente artículos sobre robótica con una experiencia centrada en el contenido. El sitio debe facilitar:

- la navegación entre la portada, los artículos y la información del autor;
- una lectura cómoda y accesible;
- la gestión del contenido por parte del editor sin depender de procesos complejos.

## Público objetivo

- Visitantes interesados en la robótica que buscan contenido claro y bien organizado.
- Editor del sitio, responsable de publicar y mantener los artículos y la presentación del autor.

## Alcance de la primera versión

### Incluido

- Portada con el nombre del blog y una lista de artículos recientes.
- Página individual para cada artículo con título, fecha, autoría y contenido.
- Sección «Sobre mí» con una breve presentación del autor.
- Navegación principal entre la portada, los artículos y la información del autor.
- Diseño adaptable, legible y accesible.
- Gestión del contenido a través del panel administrativo de Django.
- Contenido inicial de ejemplo relacionado con la robótica, que puede sustituirse o eliminarse.

### Excluido

- Cuentas públicas para lectores.
- Comentarios o interacción social.
- Suscripciones, boletines o buscador.
- Flujos editoriales avanzados.
- Funcionalidades de publicación complejas.

## Requisitos funcionales clave

### Portada y artículos recientes

La página principal mostrará el nombre del blog y una lista de artículos publicados ordenados del más reciente al más antiguo. Cada ítem incluirá título, fecha y extracto, y enlazará al artículo completo.

### Lectura de artículos

Cada artículo tendrá una página propia con:

- título;
- fecha de publicación;
- autoría;
- contenido organizado en párrafos y subtítulos.

Si la ruta solicitada no corresponde a un artículo válido, se devolverá una respuesta HTTP 404 adecuada.

### Sección «Sobre mí»

La sección presentará brevemente al autor y será accesible desde la navegación principal. El texto puede actualizarse desde el panel administrativo.

### Navegación

Las páginas públicas ofrecerán enlaces claros para volver a la portada y acceder a «Sobre mí», sin depender de JavaScript para la navegación básica.

### Gestión editorial

El editor podrá crear, editar y retirar artículos, así como actualizar la presentación del autor, mediante Django Admin. Los borradores no aparecerán en la parte pública del sitio.

## Requisitos no funcionales

- Adaptabilidad a pantallas pequeñas y grandes.
- Legibilidad mediante tipografía, contraste, espaciado y longitud de línea adecuados.
- Accesibilidad con estructuras semánticas y navegación operable con teclado.
- Rendimiento y simplicidad en renderizado del lado del servidor.
- Seguridad básica del panel administrativo de Django.

## Propuesta técnica

- Backend y renderizado: Django.
- Persistencia: modelos de Django y migraciones.
- Gestión del contenido: Django Admin.
- Interfaz: plantillas HTML semánticas y CSS adaptable.
- Base de datos inicial: SQLite para desarrollo.

## Rutas previstas

- `/` — portada con artículos recientes.
- `/sobre-mi/` — presentación del autor.
- `/articulos/<slug>/` — detalle de un artículo.
- `/admin/` — panel administrativo restringido.

## Criterios de aceptación resumidos

- Un visitante puede llegar desde la portada a un artículo y leerlo completo.
- El sitio funciona correctamente en móvil y escritorio.
- La navegación es clara y sin obstáculos.
- El editor puede mantener contenido sin editar plantillas.
- Los artículos no publicados no aparecen en la parte pública.

## Estructura del repositorio

- `PRD.md` — descripción del producto y requisitos detallados.
- `briefing.md` — resumen del contexto y objetivos del proyecto.
- `spec/` — alcance, visión y criterios de aceptación.
- `README.md` — documento de introducción y referencia del proyecto.

## Estado del proyecto

Este repositorio corresponde a la fase inicial de definición del producto. La intención es establecer una base clara para la implementación del blog antes de pasar a la construcción y validación funcional.
