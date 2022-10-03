# Generated by Django 4.1 on 2022-10-02 21:00

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGame', '0024_jugador_media_jugador_alter_jugador_contenido_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='juegos',
            name='media_juego',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='juegos',
            name='contenido_juego',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido'),
        ),
    ]
