from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

"""Tela simples de login e logout utilizando componentes do Django. 
Não foi implementado a requisição de alterar senha ou novo usuário. """


def login(request):
    if request.POST.get('submit') == 'login':
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('/')
            else:
                return render(request, 'core/login.html', {'form': form})
        return render(request, 'core/login.html', {'form': AuthenticationForm()})
    else:
        logout(request)
        return render(request, 'core/login.html', {'form': AuthenticationForm()})


def logout(request):
    if request.POST.get('submit') == 'logout':
        auth_logout(request)
    return render(request, 'core/login.html', {'form': AuthenticationForm()})
