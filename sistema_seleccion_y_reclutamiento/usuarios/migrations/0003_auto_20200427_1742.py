# Generated by Django 3.0.5 on 2020-04-27 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_aspiranteperfil_empresaperfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresaperfil',
            name='active',
        ),
        migrations.RemoveField(
            model_name='empresaperfil',
            name='name',
        ),
    ]
