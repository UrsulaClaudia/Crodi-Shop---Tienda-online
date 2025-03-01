from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ProductoViewSet, CarritoViewSet, CarritoItemViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'carrito', CarritoViewSet, basename='carrito')
router.register(r'carrito-items', CarritoItemViewSet, basename='carrito-item')

urlpatterns = [
    # path('api/', include(router.urls)),
    path('', include(router.urls)),
]