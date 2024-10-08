# Generated by Django 4.2.13 on 2024-10-10 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0026_alter_advertisementgallery_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementModeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decline_reason', models.TextField(blank=True, null=True, verbose_name='Причина почему объявление не прошло модерацию')),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderation', to='api.advertisement', verbose_name='Объявление')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderation', to=settings.AUTH_USER_MODEL, verbose_name='Риелтор')),
            ],
            options={
                'verbose_name': 'Модерация объявления',
                'verbose_name_plural': 'Модерация объявления',
            },
        ),
    ]
