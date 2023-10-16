from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Course
from .forms import RegisterForm

def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/list_courses.html', {'courses': courses})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in.
            login(request, user)
            return redirect('list_courses')
    else:
        form = RegisterForm()
    return render(request, 'registration/registration.html', {'form': form})

# need view function to redirect to course listing (/courses) or dashboard view instead of /accounts/profile

def landing(request):
    return render(request, 'registration/login_and_register.html')

