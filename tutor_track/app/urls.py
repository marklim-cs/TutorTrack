from django.urls import path
from .views import user_views, student_views, budget_views

urlpatterns = [
    path("", user_views.index, name='index'),
    path('signup/', user_views.signup, name="signup"),
    path('home/', user_views.home, name='home'),
    path('log_in/', user_views.log_in, name='log_in'),
    path('log_out/', user_views.log_out, name='log_out'),
    path("students/", student_views.StudentList.as_view(), name='students'),
    path(
        "students/<int:student_id>/",
         student_views.StudentCardView.as_view(),
         name='student_card'
         ),
    path(
        "students/<int:student_id>/<int:student_card_id>/edit/",
        student_views.UpdateStudentCard.as_view(),
        name='edit_student_card'
        ),
    path(
        "monthly_summary/",
        budget_views.MonthlyPaymentSummary.as_view(),
        name='monthly_summary'
        ),
    path("delete_summary", budget_views.DeleteSummary.as_view(), name="delete_summary")
    ]