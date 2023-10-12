from django.db import models


class Disco(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    selo_fonografico = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    pais = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
