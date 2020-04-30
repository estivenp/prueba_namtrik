# Generated by Django 3.0.5 on 2020-04-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatoria', '0003_auto_20200428_1215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='convocatoria',
            options={'ordering': ['fecha_cierre', 'hora_cierre'], 'verbose_name': 'Convocatoria', 'verbose_name_plural': 'Convocatorias'},
        ),
        migrations.RemoveField(
            model_name='convocatoria',
            name='fecha_hora_cierre',
        ),
        migrations.AddField(
            model_name='convocatoria',
            name='fecha_cierre',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='convocatoria',
            name='hora_cierre',
            field=models.TimeField(default=None),
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='estado',
            field=models.CharField(choices=[('ABIERTA', 'ABIERTA'), ('CERRADA', 'CERRADA'), ('TERMINADA', 'TERMINADA')], default='ABIERTA', max_length=10),
        ),
    ]