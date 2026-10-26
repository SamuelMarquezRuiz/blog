from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import AboutPage, Article


class PublicBlogTests(TestCase):
    def setUp(self):
        self.about_page, _ = AboutPage.objects.update_or_create(
            pk=1,
            defaults={"title": "Sobre mí", "content": "Presentación del autor."},
        )
        now = timezone.now()
        self.newest = Article.objects.create(
            title="Robots móviles",
            content="## Sensores\n\nLos sensores recogen datos.",
            author="Ana",
            is_published=True,
            excerpt="Robots que se desplazan.",
            published_at=now,
        )
        self.oldest = Article.objects.create(
            title="Automatización",
            content="Contenido publicado.",
            author="Luis",
            is_published=True,
            published_at=now - timedelta(days=1),
        )
        self.draft = Article.objects.create(
            title="Notas privadas",
            content="Este borrador no debe mostrarse.",
            author="Ana",
            is_published=False,
        )

    def test_home_shows_published_articles_newest_first(self):
        response = self.client.get(reverse("blog:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.newest.title)
        self.assertContains(response, self.oldest.title)
        self.assertNotContains(response, self.draft.title)
        self.assertLess(
            response.content.index(self.newest.title.encode()),
            response.content.index(self.oldest.title.encode()),
        )

    def test_home_shows_informative_empty_state(self):
        Article.objects.all().delete()

        response = self.client.get(reverse("blog:home"))

        self.assertContains(response, "Todavía no hay artículos publicados")

    def test_home_displays_explicit_excerpt_or_generated_summary(self):
        response = self.client.get(reverse("blog:home"))

        self.assertContains(response, self.newest.excerpt)
        self.assertContains(response, "Contenido publicado.")

    def test_article_page_displays_metadata_and_structured_content(self):
        response = self.client.get(
            reverse("blog:article-detail", kwargs={"slug": self.newest.slug})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.newest.title)
        self.assertContains(response, "Ana")
        self.assertContains(response, "<h2>Sensores</h2>", html=True)
        self.assertContains(response, "<p>Los sensores recogen datos.</p>", html=True)
        self.assertContains(response, reverse("blog:home"))

    def test_unknown_article_returns_custom_not_found_page(self):
        response = self.client.get(
            reverse("blog:article-detail", kwargs={"slug": "no-existe"})
        )

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "No encontramos esa página", status_code=404)

    def test_draft_article_is_not_publicly_accessible(self):
        response = self.client.get(
            reverse("blog:article-detail", kwargs={"slug": self.draft.slug})
        )

        self.assertEqual(response.status_code, 404)

    def test_about_page_displays_editable_presentation_and_navigation(self):
        response = self.client.get(reverse("blog:about"))

        self.assertContains(response, "Presentación del autor.")
        self.assertContains(response, "Sobre mí")
        self.assertContains(response, reverse("blog:home"))

    def test_article_content_is_escaped(self):
        self.newest.content = "<script>alert('x')</script>"
        self.newest.save()

        response = self.client.get(
            reverse("blog:article-detail", kwargs={"slug": self.newest.slug})
        )

        self.assertNotContains(response, "<script>")
        self.assertContains(response, "&lt;script&gt;")


class EditorialAccessTests(TestCase):
    def test_anonymous_visitors_are_redirected_from_admin(self):
        response = self.client.get("/admin/")

        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)

    def test_article_publication_is_a_boolean_checkbox_in_admin(self):
        article = Article.objects.create(
            title="Artículo de prueba",
            content="Contenido.",
            author="Editor",
        )
        user = get_user_model().objects.create_superuser(
            username="editor",
            email="editor@example.com",
            password="test-password",
        )
        self.client.force_login(user)

        response = self.client.get(
            reverse("admin:blog_article_change", args=[article.pk])
        )

        self.assertContains(
            response,
            f'<input type="checkbox" name="is_published"',
            html=False,
        )

    def test_staff_editor_can_manage_articles_and_about_page(self):
        user = get_user_model().objects.create_superuser(
            username="editor",
            email="editor@example.com",
            password="test-password-for-local-tests",
        )
        self.client.force_login(user)

        self.assertEqual(self.client.get("/admin/blog/article/").status_code, 200)
        self.assertEqual(self.client.get("/admin/blog/aboutpage/").status_code, 200)

    def test_about_page_is_a_single_admin_managed_record(self):
        AboutPage.objects.update_or_create(
            pk=1,
            defaults={"title": "Sobre mí", "content": "Presentación."},
        )
        user = get_user_model().objects.create_superuser(
            username="editor",
            email="editor@example.com",
            password="test-password-for-local-tests",
        )
        self.client.force_login(user)

        response = self.client.get("/admin/blog/aboutpage/add/")

        self.assertEqual(response.status_code, 403)
