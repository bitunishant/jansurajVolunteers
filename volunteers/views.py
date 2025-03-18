from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, UserProfile, AvailablePool, Team
from .forms import UserRegistrationForm, UserProfileForm, CustomAuthenticationForm

def home(request):
    return render(request, 'home.html')

from django.db import IntegrityError

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
                assign_team(profile)
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

def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("tasks")
    else:
        form = CustomAuthenticationForm()

    return render(request, "login.html", {"form": form})

@login_required
def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, "profile.html", {"profile": user_profile})

@login_required
def tasks(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})

def assign_team(volunteer):
    all_teams = Team.objects.all()
    matching_team = None

    for team in all_teams:
        if volunteer.pin_code in team.get_serving_pincodes():  # Using new method to parse CSV
            matching_team = team
            break

    if matching_team:
        volunteer.team = matching_team
        volunteer.save()
    else:
        AvailablePool.objects.create(volunteer=volunteer)

@login_required
def team_lead_dashboard(request):
    # Get the logged-in user
    user = request.user

    # Check if the user is a team lead
    team = Team.objects.filter(team_lead=user).first()

    if not team:
        return render(request, 'error.html', {'message': 'You are not a team lead!'})

    # Get all volunteers in this team
    team_members = UserProfile.objects.filter(team=team)

    # Get tasks assigned to any team member
    tasks = Task.objects.filter(assigned_to__in=team_members.values_list('user', flat=True))

    return render(request, 'team_lead_dashboard.html', {'team': team, 'team_members': team_members, 'tasks': tasks})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Team, Task, User

@login_required
def create_task(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    
    # Ensure the logged-in user is the team lead
    if request.user != team.team_lead:
        messages.error(request, "You are not authorized to create tasks for this team.")
        return redirect(request.META.get('HTTP_REFERER', f'/team-lead-dashboard/{team.id}/'))
    
    if request.method == "POST":
        title = request.POST.get("title")
        assigned_to_id = request.POST.get("assigned_to")
        assigned_to = get_object_or_404(User, id=assigned_to_id)

        # Ensure the assigned user is part of the team
        if not UserProfile.objects.filter(user=assigned_to, team=team).exists():
            messages.error(request, "Selected user is not part of the team.")
            return redirect(request.META.get('HTTP_REFERER', f'/team-lead-dashboard/{team.id}/'))

        # Create Task
        Task.objects.create(title=title, assigned_to=assigned_to, team=team)
        messages.success(request, "Task created successfully!")
        
        return redirect(request.META.get('HTTP_REFERER', f'/team-lead-dashboard/{team.id}/'))
    
    return redirect(f'/team-lead-dashboard/{team.id}/')

