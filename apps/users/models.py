from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class UserType(models.TextChoices):
        REALTOR = 'realtor', 'Риелтор'

    name = models.CharField(max_length=120, verbose_name='Имя', null=True, blank=True)
    lastname = models.CharField(max_length=120, verbose_name='Фамилия', blank=True, null=True)
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', blank=True, null=True)
    status = models.CharField(max_length=100, verbose_name='Статус', blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m', blank=True, null=True)

