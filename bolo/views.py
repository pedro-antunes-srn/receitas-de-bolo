
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Bolo
from .forms import cadastro_form, login_form,create_receita
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


def cadastros(request):
    form = cadastro_form()
    validacao = cadastro_form(request.POST)
    if request.method == "GET":
        return render(request, 'bolo/cadastro.html', {'form_cad':form})
        
    else:
        if validacao.is_valid():
            email = request.POST.get('email')
            nome = request.POST.get('nome')
            senha = request.POST.get('senha')
            user = User.objects.filter(username=nome).first()
            user_email = User.objects.filter(email=email).first()
    if user or user_email:
        return HttpResponse('Nome de usuario ou de email indisponivel')
    
    user = User.objects.create_user(username=nome, email=email, password=senha)
    user.save()
    return redirect('login')


def logviu(request):
    form = login_form()
    if request.method == "GET":
        return render(request, 'bolo/login.html',{'form_log':form})
    else:
        username = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user:
            login(request, user)
            return redirect('receitas')
        else: 
            
            return redirect('login')
        
def postagem(request):
    form = create_receita()
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'bolo/post.html',{'form':form})
        else:
            
            form = create_receita(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.criador= request.user
                post.dataq=timezone.now()
                post.save()
        
                
                return redirect('sabor')
            else:
                return redirect('postagem')
    return redirect('login')
    
def sabor(request):
    if request.user.is_authenticated:
        bolos = Bolo.objects.all()
        name = request.user.username
        return render(request, 'bolo/sabor.html', {'bolos': bolos,'name':name})
    return redirect('login')

def receita(request, slug,pk):
    if request.user.is_authenticated:
        bolo = get_object_or_404(Bolo,slug=slug,pk=pk)
        return render(request, 'bolo/receita.html', {'bolo': bolo})
    return redirect('login')

