from django.urls import path
from .views import home, register, user_login, user_logout, profile, tasks,team_lead_dashboard, create_task,complete_task

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("tasks/", tasks, name="tasks"),
    path('team-lead-dashboard/', team_lead_dashboard, name='team_lead_dashboard'),
    path('team/<int:team_id>/create-task/', create_task, name='create_task'),
     path("complete-task/<int:task_id>/", complete_task, name="complete-task"),

]
