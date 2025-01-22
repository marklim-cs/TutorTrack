from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(primary_key=True, max_length=250, null=False, unique=True)

class Books(models.Model):
    provided_id = models.CharField(max_length=100)
    title = models.CharField(max_length=500, null=False)
    subtitle = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=500, null=False)
    publisher = models.CharField(max_length=500, null=False)
    published_date = models.DateField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    distribution_expense = models.DecimalField(max_digits=20, decimal_places=2, null=False)
