import os
from django.db import models
from PIL import Image
from django.conf import settings

class Produto(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m/', null=True, blank=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField()
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples'),
        )
    )
    
    #Redimensiona a imagem
    @staticmethod
    def resize_image(img,new_width=800,max_image_size=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size     
        
        if original_width <= new_width:
            img_pil.close()
            return   
        
        new_height = round((new_width * original_height) / original_width)
        
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )
         
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.imagem:
            self.resize_image(self.imagem, max_image_size=800)
    
    def __str__(self):
        return self.nome    
    
    
class Variacao(models.Model):
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
        
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.nome or self.produto.nome