# Generated by Django 5.1.5 on 2025-01-27 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolo', '0016_remove_bolo_immagem_bolo_imagem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(height_field=50, upload_to='img', width_field=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='form_bolo',
            name='imagem',
        ),
        migrations.AlterField(
            model_name='bolo',
            name='imagem',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
