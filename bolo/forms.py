from django import forms
from django.forms import fields
from .models import Cadastro, Bolo


class cadastro_form(forms.ModelForm):
       senha = forms.CharField(widget=forms.PasswordInput)
       class Meta:
           model = Cadastro
           fields = ('email', 'nome', 'senha')
class login_form(forms.ModelForm):
       senha = forms.CharField(widget=forms.PasswordInput)
       class Meta:
           model = Cadastro
           fields = ('nome', 'senha')
    
class create_receita(forms.ModelForm):  
       class Meta:
           model = Bolo
           prepopulated_fields = {'slug': ['bolo']}
           fields = ('bolo','slug','ingredientes','calda','preparo','preparo_calda','preco','imagem') 
    
 