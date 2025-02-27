from django.contrib import admin
from .models import Usuario, Producto, Pedido, DetallePedido
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
