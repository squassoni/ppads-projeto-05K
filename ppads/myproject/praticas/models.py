from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    sobrenome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=40)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
