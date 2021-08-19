from django.urls import path
from article import views

# Completes url of 'articles/'.

urlpatterns = [
    path('create/',views.index),

]