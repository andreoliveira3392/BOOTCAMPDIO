import datetime

from tkinter import CASCADE
from django.db import models
from django.utils import timezone

class dev(models.Model):
    nome_dev = models.CharField(max_length=200)
    linguagem_preferida = models.CharField(max_length=30)
    stack = models.CharField(max_length = 100)
    modelo_trabalho = models.CharField(max_length = 50)
    cidade = models.CharField(max_length = 100)
    data_entrada = models.DateTimeField('Data de entrada')
    def __str__(self):
        return self.nome_dev



class situacao(models.Model):
    nome = models.ForeignKey(dev, on_delete=models.CASCADE)
    choice_text = models.CharField('Está Trabalhando?', max_length=200)
    def __str__(self):
        return self.choice_text
    
