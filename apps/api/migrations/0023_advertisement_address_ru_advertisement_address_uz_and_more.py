# Generated by Django 4.2.13 on 2024-09-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_consultationrequest_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='address_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='address_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='operation_type_ru',
            field=models.CharField(blank=True, choices=[('buy', 'Покупка'), ('rent', 'Аренда')], default='rent', max_length=100, null=True, verbose_name='Тип операции'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='operation_type_uz',
            field=models.CharField(blank=True, choices=[('buy', 'Покупка'), ('rent', 'Аренда')], default='rent', max_length=100, null=True, verbose_name='Тип операции'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='property_type_ru',
            field=models.CharField(choices=[('new', 'Новостройка'), ('old', 'Вторичный фонд')], max_length=100, null=True, verbose_name='Тип недвижимости'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='property_type_uz',
            field=models.CharField(choices=[('new', 'Новостройка'), ('old', 'Вторичный фонд')], max_length=100, null=True, verbose_name='Тип недвижимости'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='repair_type_ru',
            field=models.CharField(blank=True, choices=[('with', 'С ремонтом'), ('without', 'Без ремонта'), ('designed', 'Дизайнерский ремонт'), ('rough', 'Черновая'), ('pre_finished', 'Предчистовая')], max_length=100, null=True, verbose_name='Ремонт'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='repair_type_uz',
            field=models.CharField(blank=True, choices=[('with', 'С ремонтом'), ('without', 'Без ремонта'), ('designed', 'Дизайнерский ремонт'), ('rough', 'Черновая'), ('pre_finished', 'Предчистовая')], max_length=100, null=True, verbose_name='Ремонт'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='district',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Название района'),
        ),
        migrations.AddField(
            model_name='district',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Название района'),
        ),
    ]
