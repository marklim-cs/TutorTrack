from django.shortcuts import render, redirect
from django.views import View
from app.models import Student, StudentCard
from app.forms import UpdateStudentForm, UpdateStudentCardForm

class StudentList(View):
    def get(self, request):
        students = Student.objects.all().order_by('first_name')
        context = {"students": students}
        return render(request, "student_list.html", context)

class StudentCardView(View):
    def get(self, request, student_id):
        lessons = StudentCard.objects.filter(student_id=student_id)
        student = Student.objects.get(id=student_id)

        days = []
        for lesson in lessons:
            day_query = list(lesson.day.all().values())
            days.extend([entry["day"] for entry in day_query])
        context = {"student": student,
                   "days": days,
                   "lessons": lessons}
        return render(request, "student_card.html", context)

class UpdateStudentCard(View):
    def get(self, request, student_id):
        student = Student.objects.get(id=student_id)
        student_card = StudentCard.objects.get(student_id=student_id)

        student_form = UpdateStudentForm(instance=student)
        card_form = UpdateStudentCardForm(instance=student_card)

        context = {
                    "student_form": student_form,
                    "card_form": card_form,
                    "student": student,
            }

        return render(request, "edit_student_card.html", context)

    def post(self, request, student_id):
        student = Student.objects.get(id=student_id)
        student_card = StudentCard.objects.get(student_id=student_id)

        student_form = UpdateStudentForm(request.POST, instance=student)
        card_form = UpdateStudentCardForm(request.POST, instance=student_card)

        if student_form.is_valid() and card_form.is_valid():
            student_form.save()
            card_form.save()
            return redirect("app:student_card", student_id=student_id)

        else:
            context = {
                    "student_form": student_form,
                    "card_form": card_form,
                    "student": student,
            }
            return render(request, "edit_student_card", context)