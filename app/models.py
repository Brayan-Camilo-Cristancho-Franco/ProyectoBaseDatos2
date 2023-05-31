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

class TablaInicial(models.Model):
    ID_Empresa = models.IntegerField()
    Nit_Empresa = models.CharField(max_length=20)
    Nombre_Empresa = models.CharField(max_length=50)
    Direccion_Empresa = models.CharField(max_length=100)
    Sector_Empresa = models.CharField(max_length=50)
    Correo_Empresa = models.CharField(max_length=50)
    ID_Proyecto = models.IntegerField()
    Nombre_Proyecto = models.CharField(max_length=50)
    Descripcion_Proyecto = models.CharField(max_length=200)
    Fecha_Inicio_Proyecto = models.DateField()
    Fecha_Finalizacion_Proyecto = models.DateField()
    Id_Empresa_Proyecto = models.IntegerField()
    Estado_Proyecto = models.BooleanField()
    ID_M_Pago = models.IntegerField()
    Nombre_M_Pago = models.CharField(max_length=50)
    Descripcion_M_Pago = models.CharField(max_length=100)
    Estado_M_Pago = models.BooleanField()
    ID_Factura = models.IntegerField()
    Fecha_Factura = models.DateField()
    Valor_Factura = models.FloatField()
    Id_M_Pago_Factura = models.IntegerField()
    ID_T_Servicio = models.IntegerField()
    Nombre_T_Servicio = models.CharField(max_length=50)
    Descripcion_T_Servicio = models.CharField(max_length=100)
    Estado_T_Servicio = models.BooleanField()
    ID_Consultoria = models.IntegerField()
    Id_Factura_Consultoria = models.IntegerField()
    Id_T_Servicio_Consultoria = models.IntegerField()
    Estado_Consultoria = models.BooleanField()
    ID_CONS_EMP = models.IntegerField()
    id_Consultoria_CONS_EMP = models.IntegerField()
    id_Empresa_CONS_EMP = models.IntegerField()
    ID_Consultor = models.IntegerField()
    Nombre_Consultor = models.CharField(max_length=100)
    Telefono_Consultor = models.CharField(max_length=10)
    Correo_Consultor = models.CharField(max_length=50)
    Area_Especializacion_Consultor = models.CharField(max_length=50)
    ESTADO_Consultor = models.BooleanField()
    ID_CONS_CONS = models.IntegerField()
    Id_Consultoria_CONS_CONS = models.IntegerField()
    Id_Consultor_CONS_CONS = models.IntegerField()
    
    class Meta:
        db_table = 'TablaInicial'

class Prueba(models.Model):
    CODIGO_FACTURA = models.IntegerField()
    PRECIO = models.IntegerField()
    NOMBRE = models.CharField(max_length=255)

    class Meta:
        db_table = 'Prueba'