import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutPage",
            fields=[
                (
                    "id",
                    models.PositiveSmallIntegerField(
                        default=1,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(default="Sobre mí", max_length=120, verbose_name="título")),
                ("content", models.TextField(verbose_name="presentación")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="actualizado")),
            ],
            options={
                "verbose_name": "presentación del autor",
                "verbose_name_plural": "presentación del autor",
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="título")),
                ("slug", models.SlugField(blank=True, max_length=180, unique=True, verbose_name="URL")),
                ("excerpt", models.CharField(blank=True, max_length=320, verbose_name="extracto")),
                ("content", models.TextField(verbose_name="contenido")),
                ("author", models.CharField(max_length=120, verbose_name="autoría")),
                ("published_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="fecha de publicación")),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "Borrador"), ("published", "Publicado")],
                        default="draft",
                        max_length=10,
                        verbose_name="estado",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="creado")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="actualizado")),
            ],
            options={
                "verbose_name": "artículo",
                "verbose_name_plural": "artículos",
                "ordering": ("-published_at", "-pk"),
            },
        ),
    ]
