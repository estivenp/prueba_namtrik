# Generated by Django 3.0.5 on 2020-04-29 05:26

from django.db import migrations, models
import usuarios.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0013_auto_20200429_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aspiranteperfil',
            name='curriculo',
            field=models.FileField(blank=True, upload_to='curriculos', validators=[usuarios.models.validate_file_extension]),
        ),
    ]
