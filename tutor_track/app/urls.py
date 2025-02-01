from django.urls import path
from .views import user_views

urlpatterns = [
    path("", user_views.index, name="index"),
    path('signup/', user_views.signup, name="signup"),
    path('home/', user_views.home, name='home'),
    path('log_in/', user_views.log_in, name='log_in'),
    path('log_out/', user_views.log_out, name='log_out')
    ]