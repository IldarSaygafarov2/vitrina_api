from modeltranslation.translator import translator, TranslationOptions

from .models import District, Category, Advertisement


class DistrictTranslationOptions(TranslationOptions):
    fields = ('name',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class AdvertisementTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
        'address',
        'district',
        'category'
    )


translator.register(District, DistrictTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Advertisement, AdvertisementTranslationOptions)
