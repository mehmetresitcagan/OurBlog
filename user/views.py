from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def signUpUser(request):
    form = SignUpForm()
    context = {
        "form" : form
    }

    return render(request, "signUp.html", context)

def signInUser(request):
    return render(request, "signIn.html")

def signOutUser(request):
    pass
