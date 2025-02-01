from django.contrib import admin
from .models import Student, Language, Rate, Lesson

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")

class LanguageAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class RateAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "rate", "language", "tutor")

class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "rate", "date", "time")

admin.site.register(Student, StudentAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(Lesson, LessonAdmin)