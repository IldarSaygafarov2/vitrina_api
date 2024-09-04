# Generated by Django 4.2.13 on 2024-08-14 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_username',
            field=models.CharField(max_length=80, null=True, verbose_name='Юзернейм из телеграма'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[(None, ''), ('realtor', 'Риелтор'), ('simple_admin', 'Простой админ'), ('group_director', 'Руководитель')], max_length=100, null=True),
        ),
    ]