from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'id': 'username'}))
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'id': 'password'}))
