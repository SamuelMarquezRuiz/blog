from django.db import migrations


def create_initial_content(apps, schema_editor):
    Article = apps.get_model("blog", "Article")
    AboutPage = apps.get_model("blog", "AboutPage")

    AboutPage.objects.get_or_create(
        pk=1,
        defaults={
            "title": "Sobre mí",
            "content": (
                "Soy una persona apasionada por la robótica y la tecnología. "
                "En este espacio comparto ideas, proyectos y aprendizajes sobre "
                "como los robots pueden ayudarnos a comprender y transformar el mundo."
            ),
        },
    )
    Article.objects.get_or_create(
        slug="primeros-pasos-en-robotica",
        defaults={
            "title": "Primeros pasos en robótica",
            "excerpt": "Una introducción a los componentes que permiten a un robot percibir, decidir y actuar.",
            "content": (
                "La robótica combina mecánica, electrónica y programación para crear "
                "máquinas capaces de interactuar con su entorno.\n\n"
                "## Las partes de un robot\n\n"
                "Un robot suele reunir sensores para percibir el mundo, actuadores "
                "para moverse y un controlador que coordina sus acciones.\n\n"
                "## Empezar con un proyecto sencillo\n\n"
                "Un buen primer ejercicio es construir un vehículo que siga una línea. "
                "Permite experimentar con sensores, motores y decisiones programadas "
                "sin necesitar un sistema complejo."
            ),
            "author": "Equipo del blog",
            "status": "published",
        },
    )


class Migration(migrations.Migration):
    dependencies = [("blog", "0001_initial")]

    operations = [migrations.RunPython(create_initial_content, migrations.RunPython.noop)]
