# Generated by Django 4.2.1 on 2023-10-09 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='static/imagenes'),
        ),
    ]
