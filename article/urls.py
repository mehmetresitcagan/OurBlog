from django.urls import path
from article import views

# Completes url of 'articles/'.

app_name = "articles"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addArticle/', views.addArticle, name="addArticle"),
    path('article/<int:id>', views.detail, name="detail"),
]
