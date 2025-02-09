# Generated by Django 5.1.5 on 2025-01-29 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolo', '0020_remove_bolo_immagem_bolo_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolo',
            name='calda',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='bolo',
            name='ingredientes',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='bolo',
            name='preco',
            field=models.SmallIntegerField(null=True, verbose_name=' R$'),
        ),
        migrations.AlterField(
            model_name='bolo',
            name='preparo',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='bolo',
            name='preparo_calda',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
