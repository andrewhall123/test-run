from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    email=forms.EmailField(required=True, max_length=150)
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password1',
            'password2'
        ]
    def save(self, commit=True):
        user=super(SignupForm, self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]