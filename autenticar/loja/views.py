from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return HttpResponse('Loja de Cartas Pokemon')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        usuario = User.objects.filter(username=nome).first()
        if usuario:
            return HttpResponse(f'Usuário ja existe {nome}')
        
        usuario = User.objects.create_user(username=nome, password=senha)
        usuario.save()
        return HttpResponse(f'Usuário {nome} salvo com sucesso')
    

def logar(request):
    if request.method == 'GET':
        return render(request, 'logar.html')
    
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        usuario = authenticate(username=nome, password=senha)

        if usuario:
            login(request, usuario)
            return HttpResponse('Usuario autenticado')
        

        else:
            return HttpResponse('Login ou Senha invalidos')
        

@login_required(login_url='/logar')
def pagina(request):
    return HttpResponse('Página...')