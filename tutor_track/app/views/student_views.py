from django.shortcuts import render, redirect
from django.views import View
from app.models import Student, Lesson, MonthlyRecord, Language

class StudentList(View):
    def get(self, request):
        students = Student.objects.all().order_by('first_name')
        context = {"students": students}
        return render(request, "student_list.html", context)

class StudentDetail(View):
    def get(self, request, student_id):
        lessons = Lesson.objects.filter(student_id=student_id)
        student = Student.objects.get(id=student_id)

        days = []
        for lesson in lessons:
            day_query = list(lesson.day.all().values())
            days.extend([entry["day"] for entry in day_query])
        context = {"student": student,
                   "days": days,
                   "lessons": lessons}
        return render(request, "student_detail.html", context)

    def post(self, request):
        pass