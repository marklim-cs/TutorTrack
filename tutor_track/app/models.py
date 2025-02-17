from typing import List
from dataclasses import dataclass
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class StudentCardManager(models.Manager):
    def cards_by_id(self, tutor_id):
        cards = StudentCard.objects.filter(tutor=tutor_id)
        return cards

@dataclass
class StudentSummary():
    id: int
    student: str
    rate: float
    lesson_count: float
    total: float

@dataclass
class MonthlySummaryData():
    summary_per_student: List[StudentSummary]
    monthly_income: float

class MonthlySummaryManager(models.Manager):
    def detailed_monthly_summary(self, tutor_id, year, month) -> MonthlySummaryData:
        cards = StudentCard.objects.cards_by_id(tutor_id)
        monthly_summary = MonthlySummary.objects.filter(student_card__in=cards, date__year=year, date__month=month)

        summary_per_student = []
        monthly_income = 0

        for summary in monthly_summary:
            total = summary.student_card.rate * summary.lesson_count
            monthly_income += total
            summary_per_student.append(StudentSummary
                (
                    id=summary.id,
                    student=summary.student_card.student,
                    rate=summary.student_card.rate,
                    lesson_count=summary.lesson_count,
                    total=total
                )
            )

        return MonthlySummaryData(
            summary_per_student=summary_per_student,
            monthly_income=monthly_income
        )


class Student(models.Model):
    first_name = models.CharField(max_length=250, null=False)
    last_name = models.CharField(max_length=250, null=True)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Language(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Day(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class StudentCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rate = models.IntegerField(blank=True, null=True)
    day = models.ManyToManyField(Day)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = StudentCardManager()

    def __str__(self):
        return f"{self.student}, {self.rate}, {self.day}, {self.language}"

class MonthlySummary(models.Model):
    student_card = models.ForeignKey(
        StudentCard,
        on_delete=models.CASCADE,
        related_name="monthly_summary"
        )
    lesson_count = models.IntegerField(blank=False)
    date = models.DateField(default=now)

    objects = MonthlySummaryManager()

    def __str__(self):
        return f"{self.student_card}, {self.lesson_count}"