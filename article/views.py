from django.shortcuts import render
from .forms import AddArticleForm


# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def dashboard(request):
    return render(request, "dashboard.html")


def addArticle(request):
    form = AddArticleForm()
    return render(request, "addArticle.html", {"form": form})
