# Generated by Django 4.1.5 on 2023-05-28 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='conscons',
            table='CONS_CONS',
        ),
        migrations.AlterModelTable(
            name='consemp',
            table='CONS_EMP',
        ),
        migrations.AlterModelTable(
            name='consultor',
            table='CONSULTOR',
        ),
        migrations.AlterModelTable(
            name='consultoria',
            table='CONSULTORIA',
        ),
        migrations.AlterModelTable(
            name='empresa',
            table='EMPRESA',
        ),
        migrations.AlterModelTable(
            name='factura',
            table='FACTURA',
        ),
        migrations.AlterModelTable(
            name='metodopago',
            table='METODO_PAGO',
        ),
        migrations.AlterModelTable(
            name='proyecto',
            table='PROYECTO',
        ),
        migrations.AlterModelTable(
            name='tiposervicio',
            table='TIPO_SERVICIO',
        ),
    ]