from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Role


class SignUpForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "auth-box input"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Confirm password",
            "class": "auth-box input"
        })
    )

    roles = forms.ModelMultipleChoiceField(
        queryset=Role.objects.all(),
        widget=forms.SelectMultiple(attrs={
            "class": "auth-box input"
        })
    )

    class Meta:
        model = User
        fields = (
            "email",
            "full_name",
            "password1",
            "password2",
            "location",
            "roles"
        )

        widgets = {
            "email": forms.EmailInput(attrs={
                "placeholder": "Email",
                "class": "auth-box input"
            }),
            "full_name": forms.TextInput(attrs={
                "placeholder": "Full name",
                "class": "auth-box input"
            }),
            "location": forms.TextInput(attrs={
                "placeholder": "Location",
                "class": "auth-box input"
            }),

        }

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "placeholder": "Enter your email",
            "class": "auth-box input",
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Enter your password",
            "class": "auth-box input",
        })
    )

class ImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["image"]


class EditProfileForm(forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(
        queryset=Role.objects.all(),
        widget=forms.SelectMultiple(attrs={
            "class": "profile-input"
        })
    )

    class Meta:
        model = User
        fields = ['email', 'full_name', 'location', 'roles']

        widgets = {
            "email": forms.EmailInput(attrs={
                "placeholder": "Email",
                "class": "profile-input"
            }),
            "full_name": forms.TextInput(attrs={
                "placeholder": "Full name",
                "class": "profile-input"
            }),
            "location": forms.TextInput(attrs={
                "placeholder": "Location",
                "class": "profile-input"
            }),

        }

class AdoptionForm(forms.Form):
    residence = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Type of Residence",
            "class": "profile-input"
        })
    )

    number_people = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Number of people in household",
            "class": "profile-input"
        })
    )

    children = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Children",
            "class": "profile-input"
        })
    )

    dog_stay_day = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Where will the dog stay during the day?",
            "class": "profile-input"
        })
    )

    dog_sleep_night = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Where will the dog sleep at night?",
            "class": "profile-input"
        })
    )

    dog_exercise = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "How will you exercise the dog?",
            "class": "profile-input"
        })
    )

    have_owned_dog = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Have you owned a dog before?",
            "class": "profile-input"
        })
    )

    if_yes = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "If yes, what happened to you previous pets?",
            "class": "profile-input"
        })
    )

    have_you_ever = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Have you ever surrendered a pet to a shelter?",
            "class": "profile-input"
        })
    )


