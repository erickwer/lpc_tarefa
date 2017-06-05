from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    nome = models.CharField('nome', max_length=200)
    email =  models.CharField('email', max_length=200)
    senha = models.CharField('senha',max_length=200)

    def __str__(self):
        return '{}'.format(self.nome)


class Projeto(models.Model):
    nomeProjeto = models.CharField('nomeProjeto', max_length=200)

    def __str__(self):
        return '{}'.format(self.nomeProjeto)


class Tarefa(models.Model):
    nomeTarefa = models.CharField('nomeIsnc', max_length=200)
    dataEHoraDaInscricao = models.DateTimeField('dataEHoraDaInscricao', default=timezone.now)
    usuario = models.ForeignKey('Usuario')
    projeto = models.ForeignKey('Projeto')

    def __str__(self):
        return '{}'.format(self.nomeTarefa)


class ProjetoUsuario(models.Model):
    usuario = models.ForeignKey('Usuario')
    projeto = models.ForeignKey('Projeto')

    def __str__(self):
        return '{}'.format(self.nomeTarefa)
