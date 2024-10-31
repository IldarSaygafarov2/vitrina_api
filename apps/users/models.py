from django.db import models
from django.contrib.auth.models import AbstractUser


class UserType(models.TextChoices):
    REALTOR = 'realtor', 'Риелтор'
    SIMPLE_ADMIN = 'simple_admin', 'Простой админ'
    GROUP_DIRECTOR = 'group_director', 'Руководитель'

    __empty__ = ''


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', blank=True, null=True)
    tg_username = models.CharField(max_length=80, verbose_name='Юзернейм из телеграма', null=True)
    tg_user_id = models.BigIntegerField(verbose_name='ID пользователя в телеграм', null=True)
    status = models.CharField(max_length=100, verbose_name='Статус', blank=True, null=True)
    user_type = models.CharField(max_length=100, choices=UserType.choices, null=True, blank=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

