# -*- coding: utf-8 -*-
from django import forms


class RegisterForm(forms.Form):
    name=forms.CharField(required=True, min_length=2)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=20)
    phone = forms.CharField(required=True, min_length=11, max_length=11)


class LoginForm(forms.Form):
    useremail = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=20)
