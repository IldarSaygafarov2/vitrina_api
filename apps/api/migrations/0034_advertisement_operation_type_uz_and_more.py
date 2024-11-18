# Generated by Django 4.2.13 on 2024-11-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_remove_advertisement_operation_type_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='operation_type_uz',
            field=models.CharField(blank=True, choices=[('buy', 'Sotib olish'), ('rent', 'Ijara')], default='rent', max_length=100, null=True, verbose_name='Тип операции'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='property_type_uz',
            field=models.CharField(blank=True, choices=[('new', 'Yangi bino'), ('old', 'Ikkilamchi fond')], max_length=100, null=True, verbose_name='Тип недвижимости'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='repair_type_uz',
            field=models.CharField(blank=True, choices=[('with', 'Ta’mirlangan'), ('without', "Ta'mirsiz"), ('designed', 'Dizaynerlik ta’mir'), ('rough', 'Qora Suvoq'), ('pre_finished', 'Tugallanmagan ta’mir')], max_length=100, null=True, verbose_name='Ремонт'),
        ),
    ]