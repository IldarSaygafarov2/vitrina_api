from django.db import models
from django.utils.text import slugify

from apps.users.models import User


class ObjectTypeChoices(models.TextChoices):
    COMMERCIAL = 'commercial', 'Коммерческий'
    HOUSE = 'house', 'Дом'
    NEW_BUILDING = 'new_building', 'Новостройка'
    FLAT = 'flat', 'Квартира'


class ObjectTypeUzChoices(models.TextChoices):
    COMMERCIAL = 'commercial', 'Tijorat'
    HOUSE = 'house', 'Uy'
    NEW_BUILDING = 'new_building', 'Yangi bino'
    FLAT = 'flat', 'Kvartira'


class OperationTypeChoices(models.TextChoices):
    BUY = 'buy', 'Покупка'
    RENT = 'rent', 'Аренда'


class OperationTypeUzChoices(models.TextChoices):
    BUY = 'buy', 'Sotib olish'
    RENT = 'rent', 'Ijara'


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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Риелтор')
    advertisement = models.ForeignKey("Advertisement", on_delete=models.CASCADE, related_name='requests')
    is_moderated = models.BooleanField(default=False, verbose_name='Прошла модерацию?')
    rejection_reason = models.TextField(verbose_name='Причина отказа', blank=True, null=True)

    def __str__(self):
        return f'Объявление {self.advertisement.name} от {self.user}'

    class Meta:
        verbose_name = 'Объявление для модерации'
        verbose_name_plural = 'Объявления для модерации'
        ordering = ('is_moderated',)


class PropertyTypeChoices(models.TextChoices):
    NEW = 'new', 'Новостройка'
    OLD = 'old', 'Вторичный фонд'


class PropertyTypeUzChoices(models.TextChoices):
    NEW = 'new', 'Yangi bino'
    OLD = 'old', 'Ikkilamchi fond'


class RepairTypeChoices(models.TextChoices):
    WITH = 'with', 'С ремонтом'
    WITHOUT = 'without', 'Без ремонта'
    DESIGNED = 'designed', 'Дизайнерский ремонт'
    ROUGH = 'rough', 'Черновая'
    PRE_FINISHED = 'pre_finished', 'Предчистовая'


class RepairTypeUzChoices(models.TextChoices):
    WITH = 'with', 'Ta’mirlangan'
    WITHOUT = 'without', "Ta'mirsiz"
    DESIGNED = 'designed', 'Dizaynerlik ta’mir'
    ROUGH = 'rough', 'Qora Suvoq'
    PRE_FINISHED = 'pre_finished', 'Tugallanmagan ta’mir'


class Advertisement(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='districts', verbose_name='Район')
    address = models.CharField(verbose_name='Адрес', max_length=200, null=True, blank=True)

    property_type = models.CharField(
        max_length=100,
        choices=PropertyTypeChoices.choices,
        verbose_name='Тип недвижимости'
    )
    property_type_uz = models.CharField(
        max_length=100,
        choices=PropertyTypeUzChoices.choices,
        verbose_name='Тип недвижимости',
        blank=True,
        null=True
    )

    operation_type = models.CharField(
        max_length=100,
        choices=OperationTypeChoices.choices,
        null=True, blank=True,
        verbose_name='Тип операции',
        default=OperationTypeChoices.RENT
    )
    operation_type_uz = models.CharField(
        max_length=100,
        choices=OperationTypeUzChoices.choices,
        null=True, blank=True,
        verbose_name='Тип операции',
        default=OperationTypeUzChoices.RENT
    )
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
    repair_type_uz = models.CharField(
        verbose_name='Ремонт', max_length=100, choices=RepairTypeUzChoices.choices,
        null=True,
        blank=True
    )

    creation_year = models.IntegerField(verbose_name='Год постройки', default=0)
    auction_allowed = models.BooleanField(default=False, verbose_name='Торг уместен?')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='advertisements',
                                 verbose_name='Категория')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='advertisements',
                             verbose_name='Риелтор')
    is_moderated = models.BooleanField(verbose_name='Прошла модерацию?', default=False)
    house_quadrature_from = models.IntegerField(verbose_name='площадь участка от', null=True, blank=True)
    house_quadrature_to = models.IntegerField(verbose_name='площадь участка до', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for_moderation_obj, created = AdvertisementRequestForModeration.objects.get_or_create(
            user=self.user,
            advertisement=self,
        )
        if not created:
            for_moderation_obj.is_moderated = self.is_moderated

        for_moderation_obj.save()
        return

    def get_preview(self):
        gallery = self.gallery.all()
        if not gallery:
            return ''
        return gallery.first().photo.url

    def get_rooms_qty(self):
        return self.rooms_qty_from, self.rooms_qty_to

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class AdvertisementGallery(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='gallery')
    photo = models.ImageField(verbose_name='Фото', upload_to='gallery')

    class Meta:
        verbose_name = 'Фото объявления'
        verbose_name_plural = 'Фото объявлений'


class UserRequest(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    operation_type = models.CharField(verbose_name='Тип операции', max_length=100, choices=OperationTypeChoices.choices,
                                      null=True, blank=True)
    object_type = models.CharField(verbose_name='Тип объекта', max_length=100, choices=ObjectTypeChoices.choices,
                                   null=True, blank=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15)
    message = models.TextField(verbose_name='Примечание')

    def __str__(self):
        return f'{self.first_name}:{self.phone_number}'

    class Meta:
        verbose_name = 'Заявка пользователя'
        verbose_name_plural = 'Заявки пользователей'


class ConsultationRequest(models.Model):
    fullname = models.CharField(verbose_name='ФИО', max_length=100)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Заявка на консультацию'
        verbose_name_plural = 'Заявки на консультацию'
