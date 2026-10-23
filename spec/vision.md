# Visión del producto: blog de robótica

## Visión

Acercar la robótica a las personas interesadas en ella mediante un blog en español, sencillo de recorrer y agradable de leer. El sitio dará protagonismo a los artículos y a las ideas de quien los escribe, tanto en móviles como en ordenadores.

## Necesidad

Quien llega al blog necesita encontrar con facilidad las publicaciones recientes, leer cada artículo con su estructura intacta y conocer a su autor. Quien lo mantiene necesita poder actualizar artículos y presentación sin editar plantillas ni depender de un flujo editorial complejo.

## Público

- **Lectores:** personas interesadas en la robótica que buscan contenido organizado y accesible.
- **Editor:** la persona responsable de publicar y mantener los artículos y la presentación del autor.

## Propuesta de valor

Una experiencia centrada en el contenido: la portada ayuda a descubrir publicaciones, cada artículo ofrece un espacio claro para la lectura y la sección «Sobre mí» aporta contexto sobre quien escribe. La gestión mediante el panel administrativo de Django permite mantener el contenido separado de la presentación del sitio.

## Principios de experiencia

1. **La lectura primero:** priorizar el texto, una jerarquía visual clara y una longitud de línea cómoda.
2. **Navegación comprensible:** ofrecer rutas evidentes entre la portada, los artículos y «Sobre mí», sin depender de JavaScript para las acciones básicas.
3. **Accesibilidad y adaptación:** mantener contenido y navegación utilizables con teclado y en pantallas pequeñas y grandes.
4. **Publicación sencilla:** permitir que el editor gestione el contenido desde Django Admin, sin incorporar procesos editoriales avanzados.
5. **Contenido bajo control:** mostrar públicamente solo artículos publicados y ofrecer una respuesta adecuada cuando un artículo no existe.

## Resultado esperado

Una persona visitante puede descubrir un artículo desde la portada, leerlo completo y encontrar información sobre el autor sin obstáculos. El editor puede sustituir el contenido de ejemplo y mantener el blog desde el panel administrativo, sin modificar las plantillas.

## Límites de la visión

La primera versión es un blog de autor, no una comunidad ni una plataforma editorial. No contempla cuentas públicas, comentarios, suscripciones, buscador ni flujos avanzados de revisión o programación. La identidad visual definitiva, el dominio y el entorno de producción se definirán más adelante.
