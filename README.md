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

## Puesta en marcha

Requisitos: Python 3.12 o superior y Git. Ejecuta los comandos desde la carpeta raíz del repositorio.

```powershell
# Crear el entorno virtual (solo la primera vez)
python -m venv .venv

# Activarlo en PowerShell
. .\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación del script, permite scripts locales solo durante la sesión actual y vuelve a activarlo:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
. .\.venv\Scripts\Activate.ps1
```

En el Símbolo del sistema (cmd.exe), activa el entorno con:

```bat
.venv\Scripts\activate.bat
```

Con el entorno virtual activo, instala las dependencias, aplica las migraciones y arranca el servidor de desarrollo:

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` para visitar el blog. `migrate` crea o actualiza la base de datos, incluida la conversión del estado anterior a la nueva casilla booleana «Publicado», conservando qué artículos estaban publicados. La migración de contenido inicial crea una presentación de ejemplo y un artículo de robótica publicado.

Para crear una cuenta editorial local (solo es necesario hacerlo una vez por base de datos):

```powershell
python manage.py createsuperuser
```

El comando solicita un nombre de usuario, un correo electrónico y una contraseña; no hay una contraseña predeterminada. Si la cuenta ya existe y necesitas asignarle o cambiarle la contraseña, ejecuta `python manage.py changepassword nombre_de_usuario` y escribe la nueva contraseña cuando se solicite.

Después, inicia sesión en `http://127.0.0.1:8000/admin/`. En el formulario del artículo, marca «Publicado» para mostrarlo en la portada y permitir su consulta pública; desmárcalo para ocultarlo. Los artículos nuevos empiezan sin publicar. No existe registro público.

Para detener el servidor, pulsa `Ctrl+C`. Para salir del entorno virtual, ejecuta `deactivate`. El servidor `runserver` es únicamente para desarrollo, no para producción.

## Estructura del proyecto

```text
src/                    Código fuente de la aplicación
  config/               Configuración del proyecto y rutas principales
  blog/                 Aplicación de contenido del blog
    migrations/         Esquema y contenido inicial versionados
    templates/blog/     Plantillas de la experiencia pública
    static/blog/        Estilos adaptables
    templatetags/       Presentación segura del contenido de artículos
  templates/            Plantillas globales, como la página 404
spec/                   Visión, alcance y criterios de aceptación
manage.py               Herramientas de gestión de Django
requirements.txt        Dependencias de Python
db.sqlite3              Base de datos local (ignorada por Git)
```

El código ejecutable vive bajo `src/`, mientras que la documentación, dependencias, base de datos local y punto de entrada permanecen en la raíz. `manage.py` añade `src/` a la ruta de importación para que los comandos de Django sigan ejecutándose desde la raíz. La aplicación `blog` agrupa el dominio (artículos y presentación), la administración y las páginas públicas; los recursos de presentación permanecen separados. Esta organización permite añadir otras aplicaciones sin acoplarlas a las rutas o plantillas existentes. Los usuarios editoriales se guardan solo en la base de datos local y no se incluyen en el repositorio.

## Contenido y rutas

- `/` — artículos publicados, del más reciente al más antiguo.
- `/sobre-mi/` — presentación editable del autor.
- `/articulos/<slug>/` — artículo publicado.
- `/admin/` — gestión editorial, disponible solo para usuarios autorizados.

Los artículos tienen título, URL legible, extracto opcional, contenido, autoría, fecha y una casilla booleana «Publicado» (verdadero/falso) para controlar su visibilidad pública. Solo los artículos marcados aparecen en la portada y se pueden abrir desde su URL; los no publicados devuelven 404 al visitante. Si no se define un extracto, la portada genera uno a partir del contenido. Para crear subtítulos en el contenido, escribe una línea `## Subtítulo` o `### Subtítulo` y separa los párrafos con una línea en blanco. El contenido se escapa al renderizarse para no interpretar HTML introducido en el editor.

## Configuración

La configuración local usa SQLite y `DEBUG` está activado por defecto. Se pueden definir estas variables de entorno:

| Variable | Uso |
| --- | --- |
| `DJANGO_DEBUG` | Activa o desactiva el modo de depuración (`true` por defecto). |
| `DJANGO_SECRET_KEY` | Clave secreta; obligatoria cuando `DJANGO_DEBUG=false`. |
| `DJANGO_ALLOWED_HOSTS` | Lista de hosts permitidos, separados por comas. |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Orígenes HTTPS de confianza para CSRF, separados por comas. |
| `DJANGO_DB_PATH` | Ruta del archivo SQLite; por defecto `db.sqlite3`. |
| `DJANGO_SECURE_SSL_REDIRECT` | Fuerza HTTPS; activado por defecto con `DEBUG=false`. |
| `DJANGO_SECURE_HSTS_SECONDS` | Duración HSTS en segundos; un año por defecto con `DEBUG=false`. |
| `DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS` | Incluye subdominios en HSTS; actívalo solo si todos usan HTTPS. |
| `DJANGO_SECURE_HSTS_PRELOAD` | Solicita inclusión en listas preload; requiere HTTPS permanente en todos los dominios afectados. |

Antes de desplegar, desactiva `DEBUG`, establece una clave secreta fuerte, configura hosts y orígenes para el dominio real y confirma que todo el sitio se sirve por HTTPS antes de habilitar HSTS. HSTS para subdominios y preload quedan desactivados hasta confirmar que todos los dominios afectados usan HTTPS. Si un proxy gestiona HTTPS, configura la infraestructura y estos ajustes en consecuencia. Revisa la lista de comprobación de despliegue con `python manage.py check --deploy`. La base de datos de producción y el entorno de publicación siguen pendientes de definición.

## Pruebas y comprobaciones

```powershell
python manage.py check
python manage.py test blog
```

Las pruebas cubren la portada, orden y visibilidad de artículos, contenido y 404, la página «Sobre mí», el escape del contenido, la casilla booleana de publicación en el panel administrativo y el acceso editorial.
