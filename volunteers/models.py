from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    serving_pincodes = models.TextField(blank=True, help_text="Comma-separated pincodes")  # Updated to TextField
    team_lead = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="leading_teams")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_serving_pincodes(self):
        """Returns serving pincodes as a list"""
        return [p.strip() for p in self.serving_pincodes.split(",") if p.strip()]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    village = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=50, default='Bihar')
    pin_code = models.CharField(max_length=6)  # Indian pincodes are 6 digits
    contribution_area = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="volunteers")

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)  # Allow NULL values

    def __str__(self):
        return self.title



class AvailablePool(models.Model):
    volunteer = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Fallback in case `volunteer.user.username` is not available"""
        username = getattr(self.volunteer.user, "username", "Unknown")
        return f"Available: {username}"
