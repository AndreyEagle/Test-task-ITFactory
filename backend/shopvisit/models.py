from django.db import models


class Worker(models.Model):
    name = models.CharField('Имя работника', max_length=255)
    phone_number = models.CharField(
        'Номер телефона',
        max_length=255,
        unique=True
    )

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField('Название магазина', max_length=255)
    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name='shops'
    )

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name


class Visit(models.Model):
    date = models.DateTimeField(
        'Время посещения',
        auto_now_add=True,
    )
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='visit'
    )
    latitude = models.FloatField()
    longtitude = models.FloatField()

    class Meta:
        verbose_name = 'Визит'
        verbose_name_plural = 'Визиты'
