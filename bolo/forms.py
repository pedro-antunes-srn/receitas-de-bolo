from django import forms
from django.forms import fields
from .models import cadastro, login


class cadastro_form(forms.ModelForm):
       class Meta:
           model = cadastro
           fields = ('email', 'nome', 'senha')
class login_form(forms.ModelForm):
       class Meta:
           model = login
           fields = ('nome', 'senha')
    
 