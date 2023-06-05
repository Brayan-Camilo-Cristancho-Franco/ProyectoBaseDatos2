# Generated by Django 4.2.2 on 2023-06-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_empresa_creado_en_alter_empresa_modificado_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='aumento',
            field=models.FloatField(default=0.6),
        ),
        migrations.AlterField(
            model_name='consultoria',
            name='creado_en',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='consultoria',
            name='modificado_en',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='creado_en',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='modificado_en',
            field=models.DateTimeField(null=True),
        ),
    ]