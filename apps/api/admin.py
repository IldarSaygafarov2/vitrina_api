from django.contrib import admin

from . import models


class AdvertisementGalleryAdmin(admin.TabularInline):
    model = models.AdvertisementGallery
    extra = 1


class AdvertisementAdmin(admin.ModelAdmin):
    inlines = [AdvertisementGalleryAdmin]


admin.site.register(models.Advertisement, AdvertisementAdmin)
