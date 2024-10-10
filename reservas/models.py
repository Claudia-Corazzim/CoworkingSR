from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MyModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)  # Automatically set to now when created

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='sala_images/', default='default.jpg')


    def __str__(self):
        return self.nome


class Pagamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    quantia = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=50)  # Ex: "boleto", "pix", "cartao"
    boleto_url = models.URLField(max_length=200, blank=True, null=True)  # Usado para PagSeguro Boleto
    pix_info = models.TextField(blank=True, null=True)  # Informações de PIX
    esta_pago = models.BooleanField(default=False)
    data_pagamento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pagamento de {self.user} - {self.amount}'

class Feedback(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    avaliacao = models.IntegerField(default=0)
    data_feedback = models.DateTimeField(auto_now_add=True)


class Reserva(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
  data_inicio = models.DateTimeField(default=timezone.now)
  data_fim = models.DateTimeField()
  status = models.CharField(max_length=20, default='confirmada')
  sala = models.ForeignKey(Sala, on_delete=models.CASCADE, default=1) 


def __str__(self):
    return f'Reserva de {self.user} em {self.date}'
