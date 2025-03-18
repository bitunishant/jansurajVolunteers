from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)  # No choices here
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # New field added
    village = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=50, default='Bihar')
    pin_code = models.CharField(max_length=10)
    contribution_area = models.CharField(max_length=50)  # No choices here

    def __str__(self):
        return self.name
