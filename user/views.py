from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.


@csrf_exempt
def signUpUser(request):

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.success(request, "Signed up successfully.")
        return redirect("index")

    context = {
        "form": form
    }
    return render(request, "signUp.html", context)



def signInUser(request):
    return render(request, "signIn.html")


def signOutUser(request):
    pass
