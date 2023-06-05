from django.db import models
# Create your models here.
from django.db import models
from django.utils import timezone

class Empresa(models.Model):
    ID = models.AutoField(primary_key=True)
    Nit = models.CharField(max_length=20)
    Nombre = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=100)
    Sector = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)
    creado_en = models.DateTimeField()
    modificado_en = models.DateTimeField(null=True)

    class Meta:
        db_table = 'EMPRESA'

class Proyecto(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=200)
    Fecha_Inicio = models.DateField()
    Fecha_Finalizacion = models.DateField()
    Id_Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Estado = models.BooleanField()
    creado_en = models.DateTimeField()
    modificado_en = models.DateTimeField(null=True)

    class Meta:
        db_table = 'PROYECTO'

class MetodoPago(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=100)
    Estado = models.BooleanField()
    class Meta:
        db_table = 'METODO_PAGO'

class Factura(models.Model):
    ID = models.AutoField(primary_key=True)
    Fecha_Factura = models.DateField()
    Valor = models.FloatField(null=True)
    aumento = models.FloatField(default=0.6)
    Id_M_Pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)

    class Meta:
        db_table = 'FACTURA'

class TipoServicio(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=100)
    Estado = models.BooleanField()

    class Meta:
        db_table = 'TIPO_SERVICIO'

class Consultoria(models.Model):
    ID = models.AutoField(primary_key=True)
    Id_Factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    Id_T_Servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    Estado = models.BooleanField()
    creado_en = models.DateTimeField()
    modificado_en = models.DateTimeField(null=True)

    class Meta:
        db_table = 'CONSULTORIA'

class ConsEmp(models.Model):
    ID = models.AutoField(primary_key=True)
    id_Consultoria = models.ForeignKey(Consultoria, on_delete=models.CASCADE)
    id_Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now=True)
    modificado_en = models.DateTimeField(null=True)

    class Meta:
        db_table = 'CONS_EMP'

class Consultor(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=10)
    Correo = models.CharField(max_length=50)
    Area_Especializacion = models.CharField(max_length=50)
    ESTADO = models.BooleanField()
    creado_en = models.DateTimeField(default=timezone.now)
    modificado_en = models.DateTimeField(null=True)

    class Meta:
        db_table = 'CONSULTOR'

class ConsCons(models.Model):
    ID = models.AutoField(primary_key=True)
    Id_Consultoria = models.ForeignKey(Consultoria, on_delete=models.CASCADE)
    Id_Consultor = models.ForeignKey(Consultor, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)
    modificado_en = models.DateTimeField(null=True)

    class Meta:
        db_table = 'CONS_CONS'

class Ganancia(models.Model):
    ID = models.CharField(primary_key=True, max_length=36)
    Total = models.FloatField()
    Descuentos = models.FloatField()
    id_Factura = models.OneToOneField(Factura, on_delete=models.CASCADE, related_name='ganancias')
    class Meta:
        db_table = 'GANANCIA'