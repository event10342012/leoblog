# Generated by Django 3.1.5 on 2021-01-12 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_city',
            field=models.SmallIntegerField(choices=[(0, 'Taipei'), (1, 'Taichung'), (2, 'Kaohsiung')], verbose_name='job_city'),
        ),
        migrations.AlterField(
            model_name='job',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='modify_date'),
        ),
    ]
