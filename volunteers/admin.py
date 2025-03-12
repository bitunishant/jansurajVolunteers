from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'completed')
    search_fields = ('title', 'assigned_to__username')
    list_filter = ('completed',)

admin.site.register(Task, TaskAdmin)
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'district', 'state', 'contribution_area')
    search_fields = ('name', 'district', 'contribution_area')
    list_filter = ('state', 'contribution_area')
