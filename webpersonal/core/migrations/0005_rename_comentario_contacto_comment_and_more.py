# Generated by Django 4.2.1 on 2023-08-23 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_rename_nombres_completos_contacto_nombre"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contacto",
            old_name="comentario",
            new_name="comment",
        ),
        migrations.RenameField(
            model_name="contacto",
            old_name="correo",
            new_name="email",
        ),
        migrations.RenameField(
            model_name="contacto",
            old_name="nombre",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="contacto",
            old_name="producto",
            new_name="related_product",
        ),
    ]
