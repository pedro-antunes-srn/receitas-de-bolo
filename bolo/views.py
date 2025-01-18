from django.shortcuts import render
from .models import Bolo

def sabor(request):
    bolos = Bolo.objects.all()
    return render(request, 'bolo/sabor.html', {'bolos': bolos})

