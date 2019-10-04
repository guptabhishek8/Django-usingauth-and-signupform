from django.urls import path

from . import views

urlpatterns = [
    path('signup/student', views.StudentSignUp, name='studentsignup'),
    path('signup/teacher', views.TeacherSignUp, name='teachersignup'),


]
