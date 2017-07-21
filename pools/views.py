# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import LoginForm
from models import Login
from django.contrib.auth.hashers import make_password,check_password


# Create your views here.
def signup(requests):
    if requests.method == "POST":
        form = LoginForm(requests.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            data = Login(name = name,password = make_password(password))
            data.save()
            return render(requests, 'pools/response.html', {'name':name,'status': "Successfull"})

    elif requests.method == "GET":
        form = LoginForm()
        return render(requests,'pools/index.html',{'form':form})
