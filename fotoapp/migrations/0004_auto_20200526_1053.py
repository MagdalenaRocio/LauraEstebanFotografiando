# Generated by Django 2.2.12 on 2020-05-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotoapp', '0003_auto_20200526_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='respuesta5',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
