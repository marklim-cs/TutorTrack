from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import user_views, student_views, budget_views

def redirect_to_login(f):
    return login_required(f, login_url="app:log_in")

urlpatterns = [
    path("", user_views.index, name='index'),
    path('sign_up/', user_views.sign_up, name="sign_up"),
    path('home/', redirect_to_login(user_views.home), name='home'),
    path('log_in/', user_views.log_in, name='log_in'),
    path('log_out/', user_views.log_out, name='log_out'),
    path("students/", redirect_to_login(student_views.StudentList.as_view()), name='students'),
    path(
        "students/<int:student_id>/",
         redirect_to_login(student_views.StudentCardView.as_view()),
         name='student_card'
         ),
    path(
        "students/<int:student_id>/<int:student_card_id>/edit/",
        redirect_to_login(student_views.UpdateStudentCard.as_view()),
        name='edit_student_card'
        ),
    path(
        "monthly_summary/",
        redirect_to_login(budget_views.MonthlyPaymentSummary.as_view()),
        name='monthly_summary'
        ),
    path("delete_summary",
         redirect_to_login(budget_views.DeleteSummary.as_view()),
         name="delete_summary"
         ),
    path("create_student", redirect_to_login(student_views.CreateStudent.as_view()), name="create_student")
    ]