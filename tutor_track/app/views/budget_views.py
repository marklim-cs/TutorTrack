from django.views import View
from django.shortcuts import render, get_object_or_404
from app.models import MonthlySummary, Student, StudentCard
from app.forms import MonthlyPaymentForm

class MonthlyPaymentSummary(View):
    def get(self, request):
        monthly_form = MonthlyPaymentForm()

        context = {
            "monthly_form": monthly_form
        }
        return render(request, "monthly_summary.html", context)

    def post(self, request):
        pass