from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default='C',
        max_length=1,
        choices= (
        ('A', 'Aprovado'),
        ('P', 'Pendente'),
        ('C', 'Criado'),
        ('E', 'Entregue'),
        ('F', 'Finalizado'),
        ('R', 'Reprovado'),
        )
    )

    def __str__(self):
        return f'Pedido N; {self.pk}'
    

class ItemPedido(models.Model):
    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'
    
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    variacao = models.CharField(max_length=255)
    variacao_id = models.PositiveIntegerField()
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2000)
    
    def __str__(self):
        return f'Item do {self.pedido}'
    