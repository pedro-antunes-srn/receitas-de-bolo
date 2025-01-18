from django.db import models



class Bolo(models.Model):
    criador = models.CharField(max_length=30)
    bolo = models.CharField(max_length=30)
    ingredientes = models.TextField()
    preparo = models.TextField()
    preco = models.SmallIntegerField(" R$")
    slug = models.SlugField(max_length=60)
    
    def __str__(self):
        return self.bolo + '  criado por ' + self.criador
        
        
# Create your models here.
