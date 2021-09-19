from django.db import models


class Picture_colour(models.Model):
    """Model describing image and its colour parameters."""

    image = models.ImageField(
        upload_to='pic_app/',
        blank=False,
        null=False,
        verbose_name='Исследуемое изображение',
    )
    b_w_trigger = models.NullBooleanField(
        verbose_name='Больше черных (True) или белых (False) пикселей',
    )
    colour_hex = models.CharField(
        max_length=7,
        verbose_name='HEX-кодировка цвета',
    )
    colour_cnt = models.IntegerField(
        default=-1,
        verbose_name='Количество пикселей выбранного цвета',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации изображения',
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-pub_date']
