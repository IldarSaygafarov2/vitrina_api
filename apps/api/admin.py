from django.contrib import admin

from . import models


class AdvertisementGalleryAdmin(admin.TabularInline):
    model = models.AdvertisementGallery
    extra = 1


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'repair_type', 'district', 'category', 'property_type', 'auction_allowed']
    list_display_links = ['id', 'name']
    list_filter = ['repair_type', 'district', 'auction_allowed', 'property_type', 'category']
    list_editable = ['repair_type', 'district', 'auction_allowed', 'property_type', 'category']
    inlines = [AdvertisementGalleryAdmin]


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Advertisement, AdvertisementAdmin)
admin.site.register(models.District, DistrictAdmin)
admin.site.register(models.Category, CategoryAdmin)