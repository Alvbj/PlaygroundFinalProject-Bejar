# Generated by Django 4.2.5 on 2023-11-16 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Varios',
        ),
        migrations.AddField(
            model_name='instrumentos',
            name='descripcion_instrumento',
            field=models.TextField(default='Escribe una descripcion...'),
        ),
    ]
