# Generated by Django 5.1.5 on 2025-01-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolo', '0012_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nome_de_usuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='name',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
