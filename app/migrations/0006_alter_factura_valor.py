# Generated by Django 4.2.2 on 2023-06-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_ganancia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='Valor',
            field=models.FloatField(null=True),
        ),
    ]
