from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Realtor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='realtor')
    name = models.CharField(max_length=120, verbose_name='Имя')
    lastname = models.CharField(max_length=120, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    status = models.CharField(max_length=100, verbose_name='Статус')
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Риелтор'
        verbose_name_plural = 'Риелторы'

