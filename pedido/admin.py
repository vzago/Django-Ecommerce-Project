from django.contrib import admin

from . import models

class ItemPedidoInline(admin.TabularInline):
    model = models.ItemPedido
    extra = 1
    

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'total', 'status']
    search_fields = ['usuario__username', 'status']
    list_filter = ['status']
    list_editable = ['status']
    inlines = [
        ItemPedidoInline
    ]
    
admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.ItemPedido)
