from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Task, UserProfile
from .forms import UserRegistrationForm, UserProfileForm,CustomAuthenticationForm

# Home Page View
def home(request):
    return render(request, 'home.html')

from django.db import IntegrityError
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            try:
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password'])
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                messages.error(request, "A user with this email already exists.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})

# Login View
def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("tasks")  # Redirect to tasks after login
    else:
        form = CustomAuthenticationForm()

    return render(request, "login.html", {"form": form})

# Logout View
@login_required
def user_logout(request):
    logout(request)
    return redirect("login")

# Profile View
@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, "profile.html", {"profile": user_profile})

# View Assigned Tasks
@login_required
def tasks(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})
