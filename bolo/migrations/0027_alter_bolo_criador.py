# Generated by Django 5.1.5 on 2025-02-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolo', '0026_alter_bolo_criador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolo',
            name='criador',
            field=models.CharField(max_length=30),
        ),
    ]
