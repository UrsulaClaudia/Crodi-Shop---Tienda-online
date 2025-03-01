from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Usuario, Producto, Carrito, CarritoItem
from .serializers import UsuarioSerializer, ProductoSerializer, CarritoSerializer, CarritoItemSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    # Permite el acceso sin autenticacion
    permission_classes = [permissions.AllowAny]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    # Leer sin login, modificar solo autenticados
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        
        # Asigna el usuario autenticado como vendedor
        serializer.save(vendedor=self.request.user)

class CarritoViewSet(viewsets.ModelViewSet):
    serializer_class = CarritoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Carrito.objects.filter(usuario=self.request.user)
    
    def create(self, request, *args, **kwargs):
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        return Response(CarritoSerializer(carrito).data, status=status.HTTP_200_OK)
    
class CarritoItemViewSet(viewsets.ModelViewSet):
    serializer_class = CarritoItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CarritoItem.objects.filter(carrito__usuario=self.request.user)
    
    def create(self, request, *args, **kwargs):
        carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
        producto_id = request.data.get('producto')
        cantidad = int(request.data.get('cantidad', 1))

        item, created = Carrito.objects.get_or_create(carrito=carrito, producto_id=producto_id)
        if not created:
            item.cantidad += cantidad
        
        item.save()

        return Response(CarritoItemSerializer(item).data, status=status.HTTP_201_CREATED)