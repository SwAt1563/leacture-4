from django import forms
from django.contrib.auth.hashers import make_password
from .models import UserAccount
from author.models import Author



class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    author_photo = forms.ImageField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if UserAccount.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserAccount.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2

    def save(self):
        username = self.cleaned_data['username']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        author_photo = self.cleaned_data['author_photo']

        user = UserAccount(username=username, email=email)
        user.password = make_password(password)
        user.save()

        author = Author(user=user, name=name, photo=author_photo)
        author.save()

        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
