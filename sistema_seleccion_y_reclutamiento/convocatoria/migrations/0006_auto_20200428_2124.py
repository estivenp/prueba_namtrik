# Generated by Django 3.0.5 on 2020-04-29 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convocatoria', '0005_auto_20200428_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convocatoria',
            name='aspirantes',
        ),
        migrations.RemoveField(
            model_name='convocatoria',
            name='aspirantes_anonimos',
        ),
    ]
