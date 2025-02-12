from datetime import date
from django.views import View
from django.shortcuts import render, redirect, reverse
from app.models import MonthlySummary, Student, StudentCard
from app.forms import MonthlyPaymentForm


class MonthlyPaymentSummary(View):
    def get(self, request):
        current_month = date.today().month
        tutor = request.user.id
        monthly_form = MonthlyPaymentForm(tutor_id=tutor)
        cards = StudentCard.objects.filter(tutor=tutor)
        monthly_summaries = MonthlySummary.objects.filter(date__month=current_month, student_card__in=cards)

        student_totals = []
        for summary in monthly_summaries:
            total = summary.student_card.rate * summary.lesson_count
            student_totals.append({
                "id": summary.id,
                "student": summary.student_card.student, 
                "rate": summary.student_card.rate,
                "lesson_count": summary.lesson_count,
                "total": total
            })

        context = {
            "monthly_form": monthly_form,
            "student_totals": student_totals,
        }
        return render(request, "monthly_summary.html", context)

    def post(self, request):
        tutor_id = request.user.id
        monthly_form = MonthlyPaymentForm(tutor_id, request.POST)
        if monthly_form.is_valid():
            monthly_form.save()

            monthly_form = MonthlyPaymentForm(tutor_id)
            context = {
                "monthly_form": monthly_form
                }
            return redirect(reverse("app:monthly_summary"))
        else:
            context = {
                "monthly_form": monthly_form
            }
            return render(request, "monthly_summary.html", context)

class DeleteSummary(View):
    def get(self, request):
        pass

    def post(self, request):
        summary_id = request.POST.get("id")
        summary_to_delete = MonthlySummary.objects.get(id=summary_id)
        summary_to_delete.delete()

        return redirect(reverse("app:monthly_summary"))