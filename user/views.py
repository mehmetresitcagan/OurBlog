from django.shortcuts import render

# Create your views here.

def signUpUser(request):
    return render(request, "signUp.html")

def signInUser(request):
    return render(request, "signIn.html")

def signOutUser(request):
    pass
