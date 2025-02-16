from datetime import date
from django.views import View
import calendar
from django.db.models import Sum
from django.shortcuts import render, redirect, reverse
from app.models import MonthlySummary, Student, StudentCard
from app.forms import MonthlyPaymentForm

def detailed_monthly_summary(tutor_id, year, month):
    cards = StudentCard.objects.filter(tutor=tutor_id)
    monthly_summary = MonthlySummary.objects.filter(student_card__in=cards, date__year=year, date__month=month)

    summary_per_student = []
    monthly_income = 0

    for summary in monthly_summary:
        total = summary.student_card.rate * summary.lesson_count
        monthly_income += total
        summary_per_student.append(
            {
                "id": summary.id,
                "student": summary.student_card.student,
                "rate": summary.student_card.rate,
                "lesson_count": summary.lesson_count,
                "total": total
            }
        )

    context = {
        "summary_per_student": summary_per_student,
        "monthly_income": monthly_income,
    }
    return context

class CreateMonthlyPayment(View):
    def get(self, request):
        current_month = date.today().month
        current_year = date.today().year
        tutor_id = request.user.id

        monthly_form = MonthlyPaymentForm(tutor_id)
        monthly_summaries = detailed_monthly_summary(tutor_id, current_year, current_month)

        context = {
            "monthly_form": monthly_form,
            "monthly_summaries": monthly_summaries
        }
        return render(request, "monthly_payment.html", context)

    def post(self, request):
        tutor_id = request.user.id
        monthly_form = MonthlyPaymentForm(tutor_id, request.POST)
        if monthly_form.is_valid():
            monthly_form.save()

            monthly_form = MonthlyPaymentForm(tutor_id)
            context = {
                "monthly_form": monthly_form
                }
            return redirect(reverse("app:monthly_payment"))
        else:
            context = {
                "monthly_form": monthly_form
            }
            return render(request, "monthly_payment.html", context)

class DeleteSummary(View):
    def post(self, request):
        summary_id = request.POST.get("id")
        summary_to_delete = MonthlySummary.objects.get(id=summary_id)
        summary_to_delete.delete()

        return redirect(reverse("app:monthly_payment"))

class YearSummary(View):
    def get(self, request, year):
        tutor_id = request.user.id
        cards = StudentCard.objects.filter(tutor=tutor_id)
        current_year = date.today().year
        current_month = date.today().month

        summaries_by_month = []
        monthly_income = 0
        yearly_income = 0
        if year == current_year:
            for month in range(1, current_month + 1):
                summaries = MonthlySummary.objects.filter(student_card__in=cards, date__year=year, date__month=month)
                lesson_count = summaries.aggregate(Sum("lesson_count", default=0))

                for summary in summaries:
                    monthly_income += summary.student_card.rate * summary.lesson_count

                yearly_income += monthly_income
                summaries_by_month.append(
                    {
                        "month": calendar.month_name[month],
                        "lesson_count": lesson_count["lesson_count__sum"],
                        "monthly_income": monthly_income,
                    }
                )
                monthly_income = 0
        else:
            for month in range(1, 12 + 1):
                summaries = MonthlySummary.objects.filter(student_card__in=cards, date__year=year, date__month=month)
                lesson_count = summaries.aggregate(Sum("lesson_count", default=0))

                for summary in summaries:
                    monthly_income += summary.student_card.rate * summary.lesson_count

                yearly_income += monthly_income
                summaries_by_month.append(
                    {
                        "month": calendar.month_name[month],
                        "lesson_count": lesson_count["lesson_count__sum"],
                        "monthly_income": monthly_income,
                    }
                )
                monthly_income = 0

        context = {
            "summaries_by_month": summaries_by_month,
            "yearly_income": yearly_income,
            "year": year,
        }

        return render(request, "year_summary.html", context)

class MonthSummary(View):
    def get(self, request, year, month):
        tutor_id = request.user.id
        month_int = list(calendar.month_name).index(month)
        month_summary = detailed_monthly_summary(tutor_id, year, month_int)

        context = {
            "month_summary": month_summary,
            "month": month,
            "year": year,
        }

        return render(request, "month_summary.html", context)