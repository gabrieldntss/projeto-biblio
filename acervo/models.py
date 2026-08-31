from django.db import models

# Create your models here.

class acervo(models.Model):
    titulo = models.CharField(max_length=100)
    resumo = models.TextField()
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    autor = models.ForeignKey('autor', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome