# Generated by Django 4.1 on 2022-10-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGame', '0019_alter_jugador_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consola',
            name='titulo',
            field=models.CharField(max_length=50, null=True, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='juegos',
            name='titulo_posteo',
            field=models.CharField(max_length=50, null=True, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='titulo_post',
            field=models.CharField(max_length=50, null=True, verbose_name='Titulo'),
        ),
    ]
