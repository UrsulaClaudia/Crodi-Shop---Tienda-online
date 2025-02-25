from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Usuario, Producto
from .serializers import UsuarioSerializer, ProductoSerializer
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
