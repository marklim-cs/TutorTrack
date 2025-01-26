from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name='home'),
    path('log_in/', views.log_in, name='log_in')
    ]