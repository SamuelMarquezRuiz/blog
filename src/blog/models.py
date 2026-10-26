import re

from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField("título", max_length=200)
    slug = models.SlugField("URL", max_length=180, unique=True, blank=True)
    excerpt = models.CharField("extracto", max_length=320, blank=True)
    content = models.TextField("contenido")
    author = models.CharField("autoría", max_length=120)
    published_at = models.DateTimeField("fecha de publicación", default=timezone.now)
    is_published = models.BooleanField("publicado", default=False)
    created_at = models.DateTimeField("creado", auto_now_add=True)
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    class Meta:
        ordering = ("-published_at", "-pk")
        verbose_name = "artículo"
        verbose_name_plural = "artículos"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:180] or "articulo"
            candidate = base_slug
            suffix = 2
            while Article.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                suffix_text = f"-{suffix}"
                candidate = f"{base_slug[:180 - len(suffix_text)]}{suffix_text}"
                suffix += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    @property
    def summary(self):
        if self.excerpt:
            return self.excerpt
        plain_content = re.sub(r"(?m)^#{1,6}\s*", "", self.content)
        plain_content = re.sub(r"\s+", " ", plain_content).strip()
        return f"{plain_content[:217].rstrip()}..." if len(plain_content) > 220 else plain_content


class AboutPage(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, default=1, editable=False)
    title = models.CharField("título", max_length=120, default="Sobre mí")
    content = models.TextField("presentación")
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    class Meta:
        verbose_name = "presentación del autor"
        verbose_name_plural = "presentación del autor"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
