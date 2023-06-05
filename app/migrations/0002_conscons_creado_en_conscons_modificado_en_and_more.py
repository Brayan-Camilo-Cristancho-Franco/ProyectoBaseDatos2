# Generated by Django 4.2.2 on 2023-06-05 15:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conscons',
            name='creado_en',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='conscons',
            name='modificado_en',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='consemp',
            name='creado_en',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='consemp',
            name='modificado_en',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='consultor',
            name='creado_en',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='consultor',
            name='modificado_en',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='consultoria',
            name='creado_en',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='consultoria',
            name='modificado_en',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='creado_en',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='empresa',
            name='modificado_en',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='creado_en',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='modificado_en',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
