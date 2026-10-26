from django.urls import path

from .views import AboutPageView, ArticleDetailView, ArticleListView

app_name = "blog"

urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("sobre-mi/", AboutPageView.as_view(), name="about"),
    path("articulos/<slug:slug>/", ArticleDetailView.as_view(), name="article-detail"),
]
