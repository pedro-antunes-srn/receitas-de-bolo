
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Bolo
from .forms import cadastro_form, login_form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login 

def cadastros(request):
    form = cadastro_form()
    form_log = login_form()
    if request.method == "GET":
        return render(request, 'bolo/cadastro.html', {'form_cad':form})
        
    else:
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=nome).first()
        
    if user:
        return HttpResponse('Nome de usuario ou de email indisponivel')
    
    user = User.objects.create_user(username=nome, email=email, password=senha)
    user.save()
    return render(request, 'bolo/login.html',{'form_log':form_log})


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
            bolos = Bolo.objects.all()
            return redirect('sabor')
        else: 
            
            return redirect(login) 
            
            
     
   
@login_required(login_url='login')
def sabor(request):
        bolos = Bolo.objects.all()
        return render(request, 'bolo/sabor.html', {'bolos': bolos})
        

@login_required(login_url='login')
def receita(request, slug):
        bolo = get_object_or_404(Bolo, slug=slug)
        return render(request, 'bolo/receita.html', {'bolo': bolo})
    

