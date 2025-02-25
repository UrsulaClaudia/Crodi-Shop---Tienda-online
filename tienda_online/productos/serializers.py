from rest_framework import serializers
from .models import Usuario, Producto

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'direccion', 'telefono', 'es_vendedor']
    
class ProductoSerializer(serializers.ModelSerializer):
    vendedor = UsuarioSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'imagen', 'vendedor']