from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import StudentSignUpForm  ,TeacherSignUpForm

def StudentSignUp(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = StudentSignUpForm()
    return render(request, 'StudentSignUp.html', {'form': form})


def TeacherSignUp(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username , password=raw_password)
            return  redirect('login')
    else:
        form = TeacherSignUpForm()
    return render(request, 'TeacherSignUp.html', {'form': form})



