# Generated by Django 4.2.13 on 2024-09-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_consultationrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultationrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
