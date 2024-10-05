from django.db import models

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)  
    status = models.CharField(max_length=50) 
    empresa = models.CharField(max_length=150) 
    segmento = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    telefone_2 = models.CharField(max_length=20)
    cep = models.IntegerField(max_length=8)
    rua = models.CharField(max_length=150)
    numero_end = models.IntegerField(max_length=8)
    bairro = models.CharField(max_length=120)
    complemento = models.CharField(max_length=120)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    email = models.EmailField()
    instagram = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    qtd_lojas = models.IntegerField()
    prox_contato = models.DateTimeField(null=True, blank=True)
    primeiro_contato = models.DateTimeField()

class Observacoes(models.Model):
    id_observacao = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='observacoes')
    descricao = models.TextField()
    data_observacao = models.DateTimeField(auto_now_add=True)