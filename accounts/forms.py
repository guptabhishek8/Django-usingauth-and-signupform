from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class StudentSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'sap_id', 'email', 'password1', 'password2', 'role')


class TeacherSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'dept_name', 'email', 'password1', 'password2', 'role')
