from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from members.forms import UsuarioForms

def login_user(request):
    login = UsuarioForms()
    return render(request, "login_user.html", {"login": login})

def create(request):
    login= UsuarioForms(request.POST or None)    
    if login.is_valid():
        login.save()
        return redirect('index')