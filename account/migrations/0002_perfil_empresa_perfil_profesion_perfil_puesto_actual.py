# Generated by Django 5.1.2 on 2024-10-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='empresa',
            field=models.CharField(default='empresa', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='profesion',
            field=models.CharField(default='profesiomn', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='puesto_actual',
            field=models.CharField(default='puesto actual', max_length=100),
            preserve_default=False,
        ),
    ]
