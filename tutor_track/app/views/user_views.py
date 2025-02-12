from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Sum
from django.contrib import messages
from app.forms import UserRegistration
from app.models import Student, StudentCard, MonthlySummary

def index(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
        return render(request, "index.html")

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
    tutor = request.user
    students = len(Student.objects.filter(tutor=tutor.id))
    cards = StudentCard.objects.filter(tutor=tutor.id)
    cards_data = []
    total_lessons = 0
    current_month = date.today().month

    for card in cards:
        lessons = MonthlySummary.objects.filter(student_card_id=card.id, date__month=current_month).aggregate(total_lessons=Sum("lesson_count")) or {'total_lessons': 0}
        lesson_count = lessons['total_lessons'] if lessons['total_lessons'] else 0
        total_lessons += lesson_count
        
        cards_data.append({"card_id": card.id, "lessons": lesson_count})

    context = {
        "tutor": tutor,
        "students": students,
        "cards_data": cards_data,
        "total_lessons": total_lessons
    }
    return render(request, 'home.html', context)
