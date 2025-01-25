from django.contrib import admin
from .models import Category, Book

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "authors", "publisher",
                    "published_date", "distribution_expense", "category_id")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)