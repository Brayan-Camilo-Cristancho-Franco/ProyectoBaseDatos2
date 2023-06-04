from django.db import models

# Create your models here.
class Empresa(models.Model):
    ID = models.AutoField(primary_key=True)
    Nit = models.CharField(max_length=20)
    Nombre = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=100)
    Sector = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)

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
    Valor = models.FloatField()
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

    class Meta:
        db_table = 'CONSULTORIA'

class ConsEmp(models.Model):
    ID = models.AutoField(primary_key=True)
    id_Consultoria = models.ForeignKey(Consultoria, on_delete=models.CASCADE)
    id_Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CONS_EMP'

class Consultor(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=10)
    Correo = models.CharField(max_length=50)
    Area_Especializacion = models.CharField(max_length=50)
    ESTADO = models.BooleanField()

    class Meta:
        db_table = 'CONSULTOR'

class ConsCons(models.Model):
    ID = models.AutoField(primary_key=True)
    Id_Consultoria = models.ForeignKey(Consultoria, on_delete=models.CASCADE)
    Id_Consultor = models.ForeignKey(Consultor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CONS_CONS'