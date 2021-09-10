from django.db import models

# Create your models here.


class Usuario(models.Model):
    Nombre = models.CharField(max_length=50, blank= False, null=False)
    Apellido = models.CharField(max_length=50, blank= False, null=False)
    Cedula = models.CharField(max_length=10, blank= False, null=False)
    edad = models.IntegerField(blank= False, null=False)
    Direccion = models.CharField(max_length=100, blank= False, null=False)
    mail = models.EmailField(null=True,blank=True)


    usuario_creador = models.CharField(max_length=15)
    usuario_actualizador = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table="Usuario"
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"


class Cliente(models.Model):
    Nombre = models.CharField(max_length=50, blank= False, null=False)
    Apellido = models.CharField(max_length=50, blank= False, null=False)
    Cedula = models.CharField(max_length=10, blank= False, null=False)
    edad = models.IntegerField(blank= False, null=False)
    Direccion = models.CharField(max_length=100, blank= False, null=False)
    mail = models.EmailField(null=True,blank=True)


    usuario_creador = models.CharField(max_length=15)
    usuario_actualizador = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table="Cliente"
        verbose_name="Cliente"
        verbose_name_plural="Clientes"

    def __str__(self):
        return '{}{}{}'.format(self.Cedula," ",self.Nombre," ",self.Apellido)



class Nota_Venta(models.Model):
    Codigo = models.CharField(max_length=50, blank= False, null=False)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Direccion = models.CharField(max_length=100, blank= False, null=False)
    fecha = models.DateTimeField(auto_now_add=False)

    usuario_creador = models.CharField(max_length=15)
    usuario_actualizador = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table="Nota_Venta"
        verbose_name="Nota_Venta"
        verbose_name_plural="Nota_Ventas"

    def __str__(self):
        return '{}{}{}'.format(self.Codigo," ",self.Cliente," ",self.Direccion)



class Mantenimiento(models.Model):
    Codigo = models.CharField(max_length=50, blank=False, null=False)
    dispositivo = models.CharField(max_length=50, blank= False, null=False)
    sistema_Operativo = models.CharField(max_length=50, blank= False, null=False)
    descripcion = models.CharField(max_length=50, blank= False, null=False)
    Precio = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table="Mantenimiento"
        verbose_name="Mantenimiento"
        verbose_name_plural="Mantenimientos"

    def __str__(self):
        return '{}'.format(self.descripcion)


class Detalle_Nota_Venta(models.Model):
    codigo = models.ForeignKey(Nota_Venta, on_delete=models.CASCADE)
    cantidad= models.IntegerField()
    mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE)
    valor_Unitario = models.DecimalField(max_digits=5, decimal_places=2)
    valor_total = models.DecimalField(max_digits=5, decimal_places=2)

    usuario_creador = models.CharField(max_length=15)
    usuario_actualizador = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table="Detalle_Nota_Venta"
        verbose_name="Detalle_Nota_Venta"
        verbose_name_plural="Detalle_Nota_Ventas"

    def __str__(self):
        return '{}{}{}{}{}'.format(self.codigo," ", self.cantidad," ",self.mantenimiento," ",self.valor_Unitario," ",self.valor_total)


class Factura(models.Model):
    encabezado = models.ForeignKey(Nota_Venta,on_delete=models.CASCADE)
    detalle = models.ForeignKey(Detalle_Nota_Venta,on_delete=models.CASCADE)

    usuario_creador = models.CharField(max_length=15)
    usuario_actualizador = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table="Factura"
        verbose_name="Factura"
        verbose_name_plural="Facturas"

    def __str__(self):
        return '{}{}'.format(self.encabezado," ",self.detalle)











































