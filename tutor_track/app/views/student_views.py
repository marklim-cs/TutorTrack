from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from app.models import Student, StudentCard, Language
from app.forms import UpdateStudentForm, UpdateCardForm, CreateCardForm

class StudentList(View):
    def get(self, request):
        tutor_id = request.user.id
        students = Student.objects.filter(tutor_id=tutor_id).order_by('first_name')
        context = {"students": students}
        return render(request, "student_list.html", context)

class StudentCardView(View):
    def get(self, request, student_id):
        tutor_id = request.user.id
        student = Student.objects.get(id=student_id, tutor_id=tutor_id)
        student_cards = StudentCard.objects.filter(student_id=student_id, tutor_id=tutor_id)

        card_data = []
        for card in student_cards:
            days = [day.name for day in card.day.all()]
            card_data.append({"lesson": card, "days": days})

        context = {"student": student,
                   "card_data": card_data}

        return render(request, "student_card.html", context)

class UpdateStudentCard(View):
    def get(self, request, student_id, student_card_id):
        student = get_object_or_404(Student, id=student_id)
        student_card = get_object_or_404(StudentCard, student_id=student_id, id=student_card_id)

        student_form = UpdateStudentForm(instance=student)
        card_form = UpdateCardForm(instance=student_card)

        context = {
                    "student_form": student_form,
                    "card_form": card_form,
                    "student": student,
                    "student_card": student_card,
            }

        return render(request, "edit_student_card.html", context)

    def post(self, request, student_id, student_card_id):
        student = get_object_or_404(Student, id=student_id)
        student_card = get_object_or_404(StudentCard, student__id=student_id, id=student_card_id)

        student_form = UpdateStudentForm(request.POST, instance=student)
        card_form = UpdateCardForm(request.POST, instance=student_card)

        if student_form.is_valid() and card_form.is_valid():
            student_form.save()
            card_form.save()
            return redirect("app:student_card", student_id=student_id)

        else:
            context = {
                    "student_form": student_form,
                    "card_form": card_form,
                    "student": student,
            }
            return render(request, "edit_student_card", context)

class CreateStudent(View):
    def get(self, request):
        create_student_form = UpdateStudentForm()
        create_card_form = CreateCardForm()

        context = {
            "create_student_form": create_student_form,
            "create_card_form": create_card_form,
        }

        return render(request, "new_student.html", context)

    def post(self,request):
        create_student_form = UpdateStudentForm(request.POST)
        create_card_form = CreateCardForm(request.POST)

        if create_card_form.is_valid() and create_student_form.is_valid():
            student = create_student_form.save(commit=False)
            student.tutor = request.user
            student.save()

            card = create_card_form.save(commit=False)
            card.student = student
            card.tutor = student.tutor
            card.save()
            create_card_form.save_m2m()

            return redirect(reverse("app:students"))
        else:
            context = {
                "create_student_form": create_student_form, 
                "create_card_form": create_card_form,
            }
            return render(request, "new_student.html", context)

class CreateStudentCard(View):
    def get(self, request, student_id):
        card_form = UpdateCardForm()
        student = Student.objects.get(id=student_id)

        context = {
            "card_form": card_form,
            "student": student,
        }

        return render(request, "new_card.html", context)

    def post(self, request, student_id):
        card_form = UpdateCardForm(request.POST)
        student = Student.objects.get(id=student_id)
        tutor = request.user

        if card_form.is_valid():
            card = card_form.save(commit=False)
            card.student = student
            card.tutor = tutor
            card.save()
            return redirect(reverse('app:students'))

        else:
            context = {
                "card_form": card_form,
            }
            return render(request, 'new_student.html', context)

class DeleteStudent(View):
    def post(self, request):
        student_id = request.POST.get("id")
        student_to_delete = Student.objects.get(id=student_id)
        student_to_delete.delete()

        return redirect("app:students")