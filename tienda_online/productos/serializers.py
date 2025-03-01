from rest_framework import serializers
from .models import Usuario, Producto, Carrito, CarritoItem

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'direccion', 'telefono', 'es_vendedor']
    
class ProductoSerializer(serializers.ModelSerializer):
    vendedor = UsuarioSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'imagen', 'vendedor']

class CarritoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoItem
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    items = CarritoItemSerializer(many=True, read_only=True)
    class Meta:
        model = Carrito
        fields = ['id', 'usuario', 'items', 'total']