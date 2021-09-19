# Generated by Django 2.2.19 on 2021-09-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture_colour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pic_app/', verbose_name='Исследуемое изображение')),
                ('b_w_trigger', models.NullBooleanField(verbose_name='Больше черных (True) или белых (False) пикселей')),
                ('colour_hex', models.CharField(max_length=7, verbose_name='HEX-кодировка цвета')),
                ('colour_cnt', models.IntegerField(default=-1, verbose_name='Количество пикселей выбранного цвета')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации изображения')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
