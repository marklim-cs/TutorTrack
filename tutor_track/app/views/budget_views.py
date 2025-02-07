from django.views import View
from django.shortcuts import render, get_object_or_404
from app.models import MonthlyRecord, Student, StudentCard
from app.forms import MonthlyPaymentForm

class MonthlySummary(View):
    def get(self, request, student_id, student_card_id):
        student = get_object_or_404(Student, id=student_id)
        card = get_object_or_404(StudentCard, id=student_card_id, student_id=student_id)
        monthly_form = MonthlyPaymentForm(instance=card)

        context = {
            "student": student,
            "card": card,
            "monthly_form": monthly_form
        }
        return render(request, "monthly_summary.html", context)

    def post(self, request):
        pass