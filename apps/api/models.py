from django.db import models
from django.utils.text import slugify

from apps.users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class District(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название района')
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class AdvertisementRequestForModeration(models.Model):
    # class RequestStatus(models.TextChoices):
    #     MODERATION = 'moderation', 'На модерации'
    #     COMPLETED = 'completed', 'Прошло модерацию'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Риелтор')
    advertisement = models.ForeignKey("Advertisement", on_delete=models.CASCADE, related_name='requests')
    is_moderated = models.BooleanField(default=False, verbose_name='Прошла модерацию?')
    # status = models.CharField(max_length=30, choices=RequestStatus.choices, default=RequestStatus.MODERATION,
    #                           verbose_name='Статус объявления')

    def __str__(self):
        return f'Объявление {self.advertisement.name} от {self.user.first_name}'

    class Meta:
        verbose_name = 'Объявление для модерации'
        verbose_name_plural = 'Объявления для модерации'
        ordering = ('is_moderated',)



class Advertisement(models.Model):
    class PropertyTypeChoices(models.TextChoices):
        NEW = 'new', 'Новостройка'
        OLD = 'old', 'Вторичный фонд'

    class RepairTypeChoices(models.TextChoices):
        WITH = 'with', 'С ремонтом'
        WITHOUT = 'without', 'Без ремонта'
        DESIGNED = 'designed', 'Дизайнерский ремонт'
        ROUGH = 'rough', 'Черновая'
        PRE_FINISHED = 'pre_finished', 'Предчистовая'

    name = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='districts', verbose_name='Район')
    address = models.CharField(verbose_name='Адрес', max_length=200, null=True, blank=True)
    property_type = models.CharField(max_length=100, choices=PropertyTypeChoices.choices,
                                     verbose_name='Тип недвижимости')
    price = models.IntegerField(verbose_name='Цена')
    is_studio = models.BooleanField(verbose_name='Студия ?', default=False)
    rooms_qty_from = models.PositiveSmallIntegerField(verbose_name='Кол-во комнат от')
    rooms_qty_to = models.PositiveSmallIntegerField(verbose_name='Кол-во комнат до')
    quadrature_from = models.PositiveSmallIntegerField(verbose_name='Квадратура от')
    quadrature_to = models.PositiveSmallIntegerField(verbose_name='Квадратура до')
    floor_from = models.PositiveSmallIntegerField(verbose_name='Этаж от')
    floor_to = models.PositiveSmallIntegerField(verbose_name='Этаж до')
    repair_type = models.CharField(verbose_name='Ремонт', max_length=100, choices=RepairTypeChoices.choices, null=True,
                                   blank=True)
    creation_year = models.IntegerField(verbose_name='Год постройки', default=0)
    auction_allowed = models.BooleanField(default=False, verbose_name='Торг уместен?')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='advertisements',
                                 verbose_name='Категория')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='advertisements',
                             verbose_name='Риелтор')
    is_moderated = models.BooleanField(verbose_name='Прошла модерацию?', default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for_moderation = AdvertisementRequestForModeration(
            user=self.user,
            advertisement_id=self.pk,
            is_moderated=False
        )

        for_moderation.save()
        return

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class AdvertisementGallery(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='gallery')
    photo = models.ImageField(verbose_name='Фото', upload_to='gallery')


class UserRequest(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    operation_type = models.CharField(verbose_name='Тип операции', max_length=100)
    object_type = models.CharField(verbose_name='Тип объекта', max_length=100)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15)
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Примечание')

    def __str__(self):
        return f'{self.first_name}:{self.phone_number}'

    class Meta:
        verbose_name = 'Заявка пользователя'
        verbose_name_plural = 'Заявки пользователей'


