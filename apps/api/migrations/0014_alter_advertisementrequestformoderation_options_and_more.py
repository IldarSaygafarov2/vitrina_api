# Generated by Django 4.2.13 on 2024-09-17 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_advertisementrequestformoderation_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisementrequestformoderation',
            options={'ordering': ('is_moderated',), 'verbose_name': 'Объявление для модерации', 'verbose_name_plural': 'Объявления для модерации'},
        ),
        migrations.RemoveField(
            model_name='userrequest',
            name='email',
        ),
    ]