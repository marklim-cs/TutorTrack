from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=250, null=False)
    last_name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return f"{self.first_name}"

class Language(models.Model):
    name = models.CharField(max_length=250, blank=False)

class Rate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rate = models.IntegerField(blank=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)

class Lesson(models.Model):
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)