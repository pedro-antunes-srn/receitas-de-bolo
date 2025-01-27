from django.db import models



class Bolo(models.Model):
    criador = models.CharField(max_length=30)
    bolo = models.CharField(max_length=30)
    ingredientes = models.TextField()
    preparo = models.TextField()
    preco = models.SmallIntegerField(" R$")
    slug = models.SlugField(max_length=60)
    immagem = models.URLField(default='https://cooknenjoy.com/wp-content/uploads/2020/06/bolo-abobora-02.jpg')
    calda = models.TextField(null=True, blank=True)
    preparo_calda = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.bolo + '  criado por ' + self.criador
        
    
class cadastro(models.Model):
    email = models.EmailField()
    nome = models.CharField(default='', max_length=22)
    senha = models.CharField(max_length=15)
        
    def __str__(self):
         return self.nome
    
     
class login(models.Model):
    nome= models.CharField(default='', max_length=22)
    senha= models.CharField(max_length=15)
    def __str__(self):
            return self.nome
    