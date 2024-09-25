from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from . import models


class AdvertisementGalleryAdmin(admin.TabularInline):
    model = models.AdvertisementGallery
    extra = 1


class AdvertisementAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'price', 'category', 'district', 'property_type', 'repair_type']
    list_display_links = ['name', 'id']
    list_filter = ['district', 'property_type', 'category', 'repair_type']
    list_editable = ['price']
    inlines = [AdvertisementGalleryAdmin]


class DistrictAdmin(TranslationAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(TranslationAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}


class UserRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'phone_number', 'operation_type', 'object_type']
    list_display_links = ['id', 'first_name']


class AdvertisementRequestForModerationAdmin(admin.ModelAdmin):
    list_display = ['id', 'advertisement', 'user', 'is_moderated']
    list_display_links = ['id', 'advertisement']
    list_editable = ['is_moderated']
    list_filter = ['is_moderated']


class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'phone_number']
    list_display_links = ['id', 'fullname']
    list_filter = ['created_at']


admin.site.register(models.Advertisement, AdvertisementAdmin)
admin.site.register(models.District, DistrictAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.UserRequest, UserRequestAdmin)
admin.site.register(models.AdvertisementRequestForModeration, AdvertisementRequestForModerationAdmin)
admin.site.register(models.ConsultationRequest, ConsultationRequestAdmin)