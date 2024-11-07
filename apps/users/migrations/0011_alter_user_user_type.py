# Generated by Django 4.2.13 on 2024-10-31 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_tg_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[(None, ''), ('realtor', 'Риелтор'), ('simple_admin', 'Простой админ'), ('group_director', 'Руководитель')], max_length=100, null=True),
        ),
    ]