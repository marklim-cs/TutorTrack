from django.contrib import admin
from .models import Student, Language, StudentCard, MonthlySummary, Day

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")

class LanguageAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class StudentCardAdmin(admin.ModelAdmin):
    def get_days(self, obj):
        return ", ".join([day.name for day in obj.day.all()])
    get_days.short_description = 'Days'

    list_display = ("id", "student", "get_days", "rate", "language", "tutor")

class MonthlySummaryAdmin(admin.ModelAdmin):
    list_display = ("id", "student_card", "lesson_count", "date")

class DayAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(Student, StudentAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(StudentCard, StudentCardAdmin)
admin.site.register(MonthlySummary, MonthlySummaryAdmin)
admin.site.register(Day, DayAdmin)