from django.shortcuts import render, get_object_or_404

from .models import Page


def home_view(request):
    return render(request, "pages/home.html")


def about_view(request):
    obj = get_object_or_404(Page, slug="about")
    context = {
        "object": obj
    }
    return render(request, "pages/page.html", context)


def history_view(request):
    obj = get_object_or_404(Page, slug="history")
    context = {
        "object": obj
    }
    return render(request, "pages/page.html", context)


def contact_view(request):
    obj = get_object_or_404(Page, slug="contacts")
    context = {
        "object": obj
    }
    return render(request, "pages/page.html", context)
