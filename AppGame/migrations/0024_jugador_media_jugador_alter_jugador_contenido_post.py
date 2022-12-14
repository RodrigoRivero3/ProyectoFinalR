# Generated by Django 4.1 on 2022-10-02 20:59

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGame', '0023_consola_media_consola_alter_consola_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='media_jugador',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='contenido_post',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido'),
        ),
    ]
