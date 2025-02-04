
from django.conf import settings
from django.db import models    
from django.utils import timezone
class Cadastro(models.Model):
    email = models.EmailField()
    nome = models.CharField(default='', max_length=22)
    senha = models.CharField(max_length=15)
        
    def __str__(self):
         return self.nome
    
     
class Bolo(models.Model):
    criador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bolo = models.CharField(max_length=30)
    ingredientes = models.TextField(max_length=500)
    preparo = models.TextField(max_length=500)
    preco = models.SmallIntegerField(" R$", null=True)
    slug = models.SlugField(max_length=60)
    calda = models.TextField(null=True, blank=True,max_length=500)
    preparo_calda = models.TextField(null=True, blank=True,max_length=500)
    dataq = models.DateTimeField(default=timezone.now)
    imagem = models.ImageField(upload_to='media',default='')
   
    def __str__(self):
        return self.bolo
        
    