# Generated by Django 4.2.13 on 2024-10-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_delete_advertisementmoderation'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisementrequestformoderation',
            name='rejection_reason',
            field=models.TextField(blank=True, null=True, verbose_name='Причина отказа'),
        ),
    ]