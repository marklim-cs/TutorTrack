from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistration

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        registration_form = UserRegistration(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            login(request, user)
            return redirect("/home")
    else:
        registration_form = UserRegistration()

    return render(request, 'sign_up.html', {'registration_form': registration_form})

def log_in(request):
    raise NotImplementedError("TO DO")

def logout(request):
    raise NotImplementedError("TO DO")

def home(request):
    raise NotImplementedError("TO DO")

def daily_summary(request):
    raise NotImplementedError("TO DO")

def monthly_summary(reqest):
    raise NotImplementedError("TO DO")

def year_to_date_summary(request):
    raise NotImplementedError("TO DO")

def yearly_summary(request):
    raise NotImplementedError("TO DO")