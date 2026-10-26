# Criterios de aceptación: blog de robótica

Estos criterios concretan las condiciones para aceptar la primera versión descrita en el PRD, el briefing, la visión y `scope.md`. Las rutas se expresan según las propuestas actuales del PRD.

## CA-01: Portada y artículos recientes

- Al visitar `/`, se muestra el nombre del blog y una lista de artículos publicados.
- La lista está ordenada de más reciente a más antiguo según la fecha de publicación.
- Cada artículo de la lista muestra su título, fecha y extracto, y ofrece un enlace descriptivo a su página.
- Al abrir el enlace de un artículo, se muestra la página correspondiente a ese artículo.
- Si no hay artículos publicados, la portada muestra un mensaje informativo y no una lista vacía sin contexto.
- Los artículos en borrador no aparecen en la portada.

## CA-02: Lectura de un artículo

- En `/articulos/<slug>/`, la página muestra el título, la fecha de publicación, la autoría y el contenido del artículo.
- Los párrafos y subtítulos del contenido se presentan como una estructura legible y conservan su jerarquía.
- Desde la página del artículo hay un enlace claro para volver a la portada.
- Si el slug no corresponde a un artículo existente, la respuesta es HTTP 404.
- Un artículo en borrador no se puede consultar desde una ruta pública.

## CA-03: Página «Sobre mí»

- `/sobre-mi/` muestra una página identificable como «Sobre mí» y la presentación actual del autor.
- La navegación principal incluye un enlace descriptivo a esta página.
- Al actualizar la presentación desde el panel administrativo, el nuevo texto se muestra en la página pública sin modificar plantillas.

## CA-04: Navegación

- Desde las páginas públicas se puede llegar a la portada y a «Sobre mí» mediante enlaces visibles y con nombres comprensibles.
- Desde un artículo se puede volver a la portada.
- La navegación básica funciona sin JavaScript.
- Los enlaces se pueden recorrer y activar con teclado.

## CA-05: Gestión editorial y acceso

- Un editor autenticado puede crear, editar y retirar artículos desde Django Admin.
- Un editor autenticado puede actualizar la presentación del autor desde Django Admin.
- Los campos de un artículo permiten gestionar título, slug, contenido, autoría, fecha de publicación y una casilla «Publicado» (verdadero/falso).
- Tras publicar un artículo, este aparece en la portada; tras dejarlo como borrador, deja de aparecer y su ruta pública no permite leerlo.
- Una persona visitante no autenticada no puede acceder a las funciones de edición del panel administrativo.
- El sitio no ofrece registro público de lectores.
- El contenido de ejemplo sobre robótica puede sustituirse o eliminarse desde el panel administrativo.

## CA-06: Adaptabilidad, legibilidad y accesibilidad

- En pantallas pequeñas y grandes, las páginas conservan el contenido y la navegación sin desplazamiento horizontal innecesario.
- La presentación facilita la lectura mediante contraste suficiente, espaciado, jerarquía de encabezados y longitud de línea legible.
- Las páginas utilizan estructura semántica y encabezados coherentes; los enlaces describen su destino.
- La navegación y los controles disponibles se pueden utilizar con teclado.

## CA-07: Renderizado y alcance

- Las páginas informativas se renderizan en el servidor mediante Django.
- La lectura de artículos y la navegación pública no dependen de JavaScript.
- La primera versión no incluye cuentas públicas, comentarios, suscripciones, boletines, buscador, interacción social ni flujos editoriales avanzados.
