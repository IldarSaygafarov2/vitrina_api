# Generated by Django 4.2.13 on 2024-09-24 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_advertisement_address_ru_advertisement_address_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='category_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advertisements', to='api.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='category_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advertisements', to='api.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='district_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='api.district', verbose_name='Район'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='district_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='api.district', verbose_name='Район'),
        ),
    ]
