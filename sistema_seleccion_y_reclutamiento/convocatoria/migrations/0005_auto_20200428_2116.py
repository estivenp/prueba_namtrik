# Generated by Django 3.0.5 on 2020-04-29 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_auto_20200428_2114'),
        ('convocatoria', '0004_auto_20200428_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convocatoria',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.EmpresaPerfil'),
        ),
    ]