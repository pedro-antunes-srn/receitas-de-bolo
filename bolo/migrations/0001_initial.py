# Generated by Django 5.1.5 on 2025-01-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bolos', models.CharField(max_length=30)),
                ('receita', models.CharField(max_length=30)),
            ],
        ),
    ]
