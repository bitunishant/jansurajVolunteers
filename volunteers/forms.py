from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
CONTRIBUTION_CHOICES = [
    ('Education', 'Education'),
    ('Healthcare', 'Healthcare'),
    ('Environment', 'Environment'),
    ('Social Work', 'Social Work'),
]

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'input'}))
    contribution_area = forms.ChoiceField(choices=CONTRIBUTION_CHOICES, widget=forms.Select(attrs={'class': 'input'}))

    class Meta:
        model = UserProfile
        fields = ['name', 'gender', 'age', 'village', 'block', 'district', 'state', 'pin_code', 'contribution_area']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Full Name'}),
            'age': forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Age'}),
            'village': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Village'}),
            'block': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Block'}),
            'district': forms.TextInput(attrs={'class': 'input', 'placeholder': 'District'}),
            'state': forms.TextInput(attrs={'class': 'input', 'value': 'Bihar', 'readonly': True}),
            'pin_code': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Pin Code'}),
        }
