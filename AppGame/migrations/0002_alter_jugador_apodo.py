# Generated by Django 4.1 on 2022-09-05 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='apodo',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
