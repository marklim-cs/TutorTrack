from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    provided_id = models.CharField(max_length=100)
    title = models.CharField(max_length=500, null=False)
    subtitle = models.CharField(max_length=500, null=True, blank=True)
    authors = models.CharField(max_length=500, null=False)
    publisher = models.CharField(max_length=500, null=False)
    published_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    distribution_expense = models.DecimalField(max_digits=20, decimal_places=2, null=False)