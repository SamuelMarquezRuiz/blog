from django.conf import settings


def blog_settings(request):
    return {"blog_title": getattr(settings, "BLOG_TITLE", "Blog de robótica")}
