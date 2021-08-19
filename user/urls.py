from django.urls import path
from user import views

# Completes url of 'articles/'.

app_name = "article"

urlpatterns = [
    path('signIn/',views.signInUser),
    path('signUp/',views.signUpUser),
    path('signOut/', views.signOutUser),

]