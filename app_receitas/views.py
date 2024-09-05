from django.shortcuts import render

def index(request):
    return render(request, 'app_receitas/index.html')

def inicio(request):
    return render(request, 'app_receitas/inicio.html')

def contato(request):
    return render(request, 'app_receitas/contato.html')

def quemsomos(request):
    return render(request, 'app_receitas/quemsomos.html')

def login(request):
    return render(request, 'app_receitas/login.html')

def politicaprivacidade(request):
    return render(request, 'app_receitas/politicaprivacidade.html')