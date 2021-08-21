from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddArticleForm
from django.contrib import messages
from .models import Article


# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def dashboard(request):
    articles = Article.objects.filter()
    context = {
        "articles" : articles
    }
    return render(request, "dashboard.html", context)


def addArticle(request):
    form = AddArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Article has been created successfully.")
        return redirect("index")
    return render(request, "addArticle.html", {"form": form})


def detail(request, id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id=id)
    context = {
        "article" : article
    }
    return render(request, "detail.html", context)
