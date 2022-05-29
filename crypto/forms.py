# imports django forms, user and userCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# creates signup form, ensures details are saved and the form is cleared if all the inputs are valid

class Signup(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(Signup, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user
