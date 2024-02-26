from django.shortcuts import render, redirect
from members.forms import UsuarioForms
from ativos.models import Ativo

def login_user(request):
    login = UsuarioForms()
    return render(request, "login_user.html", {"login_template": login})

def create(request):
    login = UsuarioForms(request.POST or None)    
    if login.is_valid():
        login.save()
        return redirect('index') #TODO: esse index redireciona para onde? para o path com name="index" na url?
    

def history(request):
    ativos = Ativo.objects.all()
    return render(request, 'history.html', {'ativos': ativos})
                                    

def configuration(request):
    return render(request, 'configuration.html')