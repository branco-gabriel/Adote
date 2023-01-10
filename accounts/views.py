from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect



def register(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if len(name.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0 or len(confirm_password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'PREENCHA TODOS OS CAMPOS')
            return render(request, 'register.html')
        
        if password != confirm_password:
            messages.add_message(request, constants.ERROR, 'AS SENHA SÃO DIFERENTES!')
            return render(request, 'register.html')
        try:
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password,
            )
            messages.add_message(request, constants.SUCCESS, 'USUÁRIO CADASTRADO COM SUCESSO!')
            return render(request,'register.html')
        except:
            messages.add_message(request, constants.ERROR, 'ERRO INTERNO!')
            return render(request,'register.html')
        


def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else:
            messages.add_message(request, constants.ERROR, 'USUARIO OU SENHA INVALIDOS!')
            return render(request, 'login.html')

        return HttpResponse(f'{name}, {password}')


def log_out(request):
    logout(request)
    return redirect('/accounts/login')