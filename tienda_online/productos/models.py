from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuario(AbstractUser):
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15,blank=True, null=True)
    es_vendedor = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Enviado', 'Enviado'), ('Completado', 'Completado')], default='Pendiente')

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.username}'
    
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.producto.nombre} x {self.cantidad}'