# Generated by Django 5.1.2 on 2024-10-25 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_alter_publicacion_requisitos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='requisitos',
            new_name='re_requisitos',
        ),
    ]
