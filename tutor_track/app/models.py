from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=250, null=False)
    last_name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Language(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Day(models.Model):
    day = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.day}"

class Lesson(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rate = models.IntegerField(blank=True, null=True)
    day = models.ManyToManyField(Day)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.student}, {self.rate}, {self.day}, {self.language}"

class MonthlyRecord(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    count = models.IntegerField(blank=False)
    total_money = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.lesson}, {self.count}, {self.total_money}"