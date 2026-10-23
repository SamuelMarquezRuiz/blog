# Alcance del producto: blog de robótica

## Objetivo

Definir la primera versión del blog de robótica en español. El producto debe facilitar que los visitantes descubran y lean artículos y conozcan a quien los escribe, y permitir que el editor mantenga el contenido sin modificar las plantillas.

## Usuarios incluidos

- **Visitante:** consulta los artículos publicados y la presentación del autor. No necesita cuenta.
- **Editor del sitio:** crea, actualiza y retira artículos, y mantiene la presentación del autor mediante el panel administrativo de Django.

## Incluido en la primera versión

### Experiencia pública

- Portada en `/` con el nombre del blog y artículos publicados, ordenados del más nuevo al más antiguo.
- Cada elemento de la portada presenta título, fecha, extracto y enlace al artículo completo.
- Mensaje informativo cuando todavía no haya artículos publicados.
- Página individual en `/articulos/<slug>/` con título, fecha, autoría y contenido organizado en párrafos y subtítulos.
- Respuesta HTTP 404 adecuada para artículos inexistentes.
- Página «Sobre mí» en `/sobre-mi/`, con una presentación editable del autor.
- Navegación clara entre la portada, los artículos y «Sobre mí»; desde un artículo se puede volver a la portada.

### Gestión de contenido

- Panel administrativo estándar de Django en `/admin/`, accesible solo para usuarios autorizados.
- Gestión de artículos y de una presentación principal del autor.
- Artículos con título, slug, contenido, autoría, fecha de publicación y estado de publicación.
- Solo los artículos publicados aparecen en las páginas públicas; el editor puede gestionar los borradores desde el panel.
- Contenido inicial de ejemplo sobre robótica, sustituible o eliminable desde el panel.
- No se ofrece registro público.

### Calidad y presentación

- Sitio adaptable a móviles y ordenadores, sin desplazamiento horizontal innecesario.
- Diseño centrado en la lectura, con tipografía, contraste, espaciado y longitud de línea legibles.
- HTML semántico, encabezados coherentes, enlaces descriptivos y navegación utilizable con teclado.
- Renderizado en el servidor mediante Django; JavaScript no es necesario para la navegación básica.

## Fuera de alcance

- Cuentas, perfiles o registro para lectores.
- Comentarios o interacción social.
- Suscripciones o boletines.
- Buscador.
- Flujos editoriales avanzados, como revisión, programación de publicaciones o múltiples roles.
- Aplicación móvil nativa o dependencia de JavaScript para las funciones básicas.
- Definición de dominio, identidad visual definitiva o configuración de despliegue de producción.
- Selección definitiva de una base de datos de producción.

## Límites técnicos

- Django se utilizará para el backend y el renderizado de páginas.
- Los artículos y la presentación del autor se persistirán mediante modelos y migraciones de Django.
- SQLite se contempla para el desarrollo inicial; la base de datos de producción queda pendiente del entorno de despliegue.
- El panel administrativo no debe permitir operaciones de edición a visitantes anónimos y la configuración de producción deberá seguir las prácticas de seguridad de Django.

## Supuestos y decisiones pendientes

- El contenido tratará sobre robótica y el idioma inicial será el español.
- La primera versión contempla un editor y una única presentación principal del autor.
- El contenido de ejemplo es provisional y podrá reemplazarse desde el panel administrativo.
- La estructura de aplicaciones, las versiones de Django, el dominio, la identidad visual y el entorno de despliegue se concretarán durante la implementación.

## Criterio de cierre del alcance

La primera versión estará dentro del alcance cuando un visitante pueda encontrar un artículo publicado desde la portada, leerlo completo, volver a la portada y consultar «Sobre mí» en móvil o escritorio; y cuando el editor pueda gestionar artículos y presentación desde el panel sin editar plantillas. Los artículos no publicados deben permanecer fuera del sitio público.
