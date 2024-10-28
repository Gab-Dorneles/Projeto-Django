from django.db import models # type: ignore

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2,max_digits=8)
    estoque = models.IntegerField()
    def __str__(self):
     return f"{self.nome} R$ {self.preco}"

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    cpf = models.IntegerField()
    def __str__(self):
     return self.nome