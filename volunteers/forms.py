from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
CONTRIBUTION_CHOICES = [
    ('Education', 'Education'),
    ('Healthcare', 'Healthcare'),
    ('Environment', 'Environment'),
    ('Social Work', 'Social Work'),
]

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500",
        "placeholder": "Enter your username"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500",
        "placeholder": "Enter your email"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500",
        "placeholder": "Enter your password"
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={
        'class': "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500"
    }))
    contribution_area = forms.ChoiceField(choices=CONTRIBUTION_CHOICES, widget=forms.Select(attrs={
        'class': "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500"
    }))

    class Meta:
        model = UserProfile
        fields = ['name', 'gender', 'age', 'village', 'block', 'district', 'state', 'pin_code', 'contribution_area']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500",
                'placeholder': 'Full Name'
            }),
            'age': forms.NumberInput(attrs={
                'class': "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500",
                'placeholder': 'Age'
            }),
            'village': forms.TextInput(attrs={
                'class': "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500",
                'placeholder': 'Village'
            }),
            'block': forms.TextInput(attrs={
                'class': "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500",
                'placeholder': 'Block'
            }),
            'district': forms.TextInput(attrs={
                'class': "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500",
                'placeholder': 'District'
            }),
            'state': forms.TextInput(attrs={
                'class': "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500",
                'value': 'Bihar',
                'readonly': True
            }),
            'pin_code': forms.TextInput(attrs={
                'class': "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500",
                'placeholder': 'Pin Code'
            }),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500",
        "placeholder": "Enter your username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input w-full border border-gray-300 rounded-lg px-4 py-2 text-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500",
        "placeholder": "Enter your password"
    }))
