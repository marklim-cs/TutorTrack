from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=250, null=False)
    last_name = models.CharField(max_length=250, null=True)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)

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
    def __str__(self):
        return f"{self.student}, {self.rate}, {self.day}, {self.language}"

class MonthlySummary(models.Model):
    student_card = models.ForeignKey(StudentCard, on_delete=models.CASCADE)
    lesson_count = models.IntegerField(blank=False)
    date = models.DateField(default=now)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_card}, {self.lesson_count}"