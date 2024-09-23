from django.db import models

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)  
    status = models.CharField(max_length=50) 
    empresa = models.CharField(max_length=150) 
    segmento = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    email = models.EmailField()
    instagram = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    qtd_lojas = models.IntegerField()
    observacoes = models.TextField()
    prox_contato = models.DateField() 
    primeiro_contato = models.DateTimeField(auto_now_add=True)

