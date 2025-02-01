from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from app.forms import UserRegistration

def signup(request):
    if request.method == "POST":
        registration_form = UserRegistration(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            login(request, user)
            return redirect("/home")
    else:
        registration_form = UserRegistration()

    return render(request, 'signup.html', {'registration_form': registration_form})

def log_in(request):
    if request.method == "POST":
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("/home")
    else:
        login_form = AuthenticationForm()

    return render(request, "log_in.html", {"login_form": login_form})


def log_out(request):
    logout(request)
    messages.success(request, "You've successfully logged out. We hope to see you soon!")
    return render(request, "log_out.html")

def home(request):
    return render(request, 'home.html')
