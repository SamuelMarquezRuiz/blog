from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView

from .models import AboutPage, Article


class ArticleListView(ListView):
    model = Article
    template_name = "blog/home.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class AboutPageView(TemplateView):
    template_name = "blog/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_page"] = get_object_or_404(AboutPage, pk=1)
        return context


def page_not_found(request, exception):
    return render(request, "404.html", status=404)
