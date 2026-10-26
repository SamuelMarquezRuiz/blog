from django.db import migrations, models


def copy_status_to_publication_flag(apps, schema_editor):
    Article = apps.get_model("blog", "Article")
    Article.objects.using(schema_editor.connection.alias).filter(
        status="published"
    ).update(is_published=True)


def copy_publication_flag_to_status(apps, schema_editor):
    Article = apps.get_model("blog", "Article")
    Article.objects.using(schema_editor.connection.alias).filter(
        is_published=True
    ).update(status="published")


class Migration(migrations.Migration):
    dependencies = [("blog", "0002_initial_content")]

    operations = [
        migrations.AddField(
            model_name="article",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="publicado"),
        ),
        migrations.RunPython(
            copy_status_to_publication_flag,
            copy_publication_flag_to_status,
        ),
        migrations.RemoveField(
            model_name="article",
            name="status",
        ),
    ]
