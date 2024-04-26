# Generated by Django 5.0.4 on 2024-04-26 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('contenido', models.TextField()),
                ('categoria', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm.autor')),
            ],
        ),
    ]