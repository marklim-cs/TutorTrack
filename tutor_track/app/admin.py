from django.contrib import admin
from .models import Student, Language, StudentCard, MonthlyRecord, Day

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

class MonthlyRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "lesson", "count", "total_money")

class DayAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(Student, StudentAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(StudentCard, StudentCardAdmin)
admin.site.register(MonthlyRecord, MonthlyRecordAdmin)
admin.site.register(Day, DayAdmin)