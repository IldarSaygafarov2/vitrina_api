# Generated by Django 4.2.13 on 2024-08-08 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='gallery', verbose_name='Фото')),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='api.advertisement')),
            ],
        ),
    ]
