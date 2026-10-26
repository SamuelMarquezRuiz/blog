from django.contrib import admin

from .models import AboutPage, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_published", "published_at", "updated_at")
    list_filter = ("is_published", "published_at")
    search_fields = ("title", "excerpt", "content", "author")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    ordering = ("-published_at",)
    fieldsets = (
        ("Contenido", {"fields": ("title", "slug", "excerpt", "content", "author")}),
        ("Publicación", {"fields": ("is_published", "published_at")}),
    )


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    fields = ("title", "content")

    def has_add_permission(self, request):
        return not AboutPage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
