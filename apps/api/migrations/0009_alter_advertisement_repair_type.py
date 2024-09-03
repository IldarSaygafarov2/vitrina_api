# Generated by Django 4.2.13 on 2024-09-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_userrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='repair_type',
            field=models.CharField(choices=[('with', 'С ремонтом'), ('without', 'Без ремонта'), ('designed', 'Дизайнерский ремонт'), ('rough', 'Черновая'), ('pre_finished', 'Предчистовая')], default='with', max_length=100, verbose_name='Ремонт'),
        ),
    ]
