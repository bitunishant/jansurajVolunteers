from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.utils.html import format_html
from django.urls import path
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Task, UserProfile, AvailablePool, Team

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'assigned_to', 'team','completed')
    search_fields = ('title', 'assigned_to__username')
    list_filter = ('completed',)

admin.site.register(Task, TaskAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'name', 'district', 'state', 'contribution_area', 'team')
    search_fields = ('name', 'district', 'contribution_area')
    list_filter = ('state', 'contribution_area', 'team')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'team_lead', 'pincode_list', 'description_preview')
    search_fields = ('name', 'team_lead__username', 'serving_pincodes')
    list_filter = ('team_lead',)  # Filter by team leads
    def pincode_list(self, obj):
        """Show serving pincodes as a string"""
        return obj.serving_pincodes
    pincode_list.short_description = "Serving Pincodes"

    def description_preview(self, obj):
        return obj.description[:50] + "..." if obj.description else "-"
    description_preview.short_description = "Description"

@admin.register(AvailablePool)
class AvailablePoolAdmin(admin.ModelAdmin):
    list_display = ('volunteer', 'assign_team_link')
    search_fields = ('volunteer__user__username', 'volunteer__pin_code')

    def assign_team_link(self, obj):
        return format_html('<a href="assign-team/{}/">Assign to Team</a>', obj.id)
    assign_team_link.short_description = "Assign Team"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('assign-team/<int:pool_id>/', self.admin_site.admin_view(self.assign_team))
        ]
        return custom_urls + urls

    def assign_team(self, request, pool_id):
        available_user = get_object_or_404(AvailablePool, id=pool_id)
        user_profile = available_user.volunteer
    
        all_teams = Team.objects.all()
        matching_team = None
    
        for team in all_teams:
            print(team.get_serving_pincodes())
            print(user_profile.pin_code)

            if user_profile.pin_code in team.get_serving_pincodes():  # Using new method
                matching_team = team
                break
            
        if matching_team:
            user_profile.team = matching_team
            user_profile.save()
            available_user.delete()
            messages.success(request, f"{user_profile.user.username} assigned to {matching_team.name}")
        else:
            messages.error(request, "No matching team found for this user.")
    
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))
