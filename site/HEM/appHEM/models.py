from django.db import models

# Create your models here.

class Paciente(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    email = models.CharField(max_length=256, blank=False, null=False)
    nome = models.TextField(max_length=50, blank=False, null=False)
    senha = models.CharField(max_length=30, blank=False, null=False)

class Medico(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    email = models.CharField(max_length=256, blank=False, null=False)
    nome = models.TextField(max_length=50, blank=False, null=False)
    senha = models.CharField(max_length=30, blank=False, null=False)
    crm = models.CharField(max_length=8, blank=False, null=False)
    especialidade = models.TextField(max_length=120, blank=False, null=False)