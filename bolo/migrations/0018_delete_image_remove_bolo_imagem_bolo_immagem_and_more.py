# Generated by Django 5.1.5 on 2025-01-27 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolo', '0017_image_remove_form_bolo_imagem_alter_bolo_imagem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='image',
        ),
        migrations.RemoveField(
            model_name='bolo',
            name='imagem',
        ),
        migrations.AddField(
            model_name='bolo',
            name='immagem',
            field=models.URLField(default='https://cooknenjoy.com/wp-content/uploads/2020/06/bolo-abobora-02.jpg'),
        ),
        migrations.AddField(
            model_name='form_bolo',
            name='immagem',
            field=models.URLField(default='https://cooknenjoy.com/wp-content/uploads/2020/06/bolo-abobora-02.jpg'),
        ),
    ]
