from django import forms
from django.forms import ModelForm
from django.forms.widgets import NumberInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Student, StudentCard, Language, Day, MonthlySummary

class UserRegistration(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UpdateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']

class UpdateStudentCardForm(ModelForm):
    day = forms.ModelMultipleChoiceField(queryset=Day.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)
    language = forms.ModelChoiceField(queryset=Language.objects.all(), required=True)

    class Meta:
        model = StudentCard
        fields = ['rate', 'day', 'language']

class MonthlyPaymentForm(ModelForm):
    date = forms.DateField(widget=NumberInput(attrs={"type":"date"}))
    class Meta:
        model = MonthlySummary
        fields = ['student_card', 'lesson_count', 'date']