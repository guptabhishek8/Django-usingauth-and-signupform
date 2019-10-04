from django.contrib import admin

from .models import CustomUser
from .forms import StudentSignUpForm


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    model = CustomUser
    add_form = StudentSignUpForm
    list_display = ['username', 'first_name', 'last_name', 'email', 'dept_name', 'sap_id', 'role']


admin.site.register(CustomUser, StudentAdmin)
