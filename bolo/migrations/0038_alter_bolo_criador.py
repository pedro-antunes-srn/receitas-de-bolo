# Generated by Django 5.1.5 on 2025-02-03 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolo', '0037_alter_bolo_criador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolo',
            name='criador',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='bolo.cadastro'),
        ),
    ]
