# Generated by Django 4.2.13 on 2024-08-14 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_lastname_user_name_user_phone_number_user_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[(None, ''), ('realtor', 'Риелтор'), ('simple_admin', 'Простой админ'), ('group_director', 'Руководитель')], max_length=100, null=True),
        ),
    ]