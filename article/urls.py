from django.urls import path
from article import views

# Completes url of 'articles/'.

app_name = "article"

urlpatterns = [
    path('create/',views.index),

]