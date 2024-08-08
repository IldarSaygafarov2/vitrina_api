from django.db import models
from apps.users.models import Realtor


class District(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название района')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class Advertisement(models.Model):
    class PropertyTypeChoices(models.TextChoices):
        NEW = 'new', 'Новостройка'
        OLD = 'old', 'Вторичный фонд'

    class RepairTypeChoices(models.TextChoices):
        WITH = 'with', 'С ремонтом'
        WITHOUT = 'without', 'Коробка без ремонта'

    name = models.CharField(max_length=100)
    description = models.TextField(verbose_name='Описание')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='districts', verbose_name='Район')
    property_type = models.CharField(max_length=100, choices=PropertyTypeChoices.choices, verbose_name='Тип недвижимости')
    price = models.IntegerField(verbose_name='Цена')
    rooms_qty_from = models.PositiveSmallIntegerField(verbose_name='Кол-во комнат от')
    rooms_qty_to = models.PositiveSmallIntegerField(verbose_name='Кол-во комнат до')
    quadrature_from = models.PositiveSmallIntegerField(verbose_name='Квадратура от')
    quadrature_to = models.PositiveSmallIntegerField(verbose_name='Квадратура до')
    floor_from = models.PositiveSmallIntegerField(verbose_name='Этаж от')
    floor_to = models.PositiveSmallIntegerField(verbose_name='Этаж до')
    repair_type = models.CharField(verbose_name='Ремонт', max_length=100)
    auction_allowed = models.BooleanField(default=False, verbose_name='Торг уместен?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class AdvertisementGallery(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='gallery')
    photo = models.ImageField(verbose_name='Фото', upload_to='gallery')