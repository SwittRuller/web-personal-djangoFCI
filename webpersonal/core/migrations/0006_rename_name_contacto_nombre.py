# Generated by Django 4.2.1 on 2023-08-23 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_rename_comentario_contacto_comment_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contacto",
            old_name="name",
            new_name="nombre",
        ),
    ]
