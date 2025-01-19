from django.shortcuts import render, get_object_or_404  
from .models import Bolo

def sabor(request):
    bolos = Bolo.objects.all()
    return render(request, 'bolo/sabor.html', {'bolos': bolos})

def receita(request, slug):
    bolo = get_object_or_404(Bolo, slug=slug)
    return render(request, 'bolo/receita.html', {'bolo': bolo})

