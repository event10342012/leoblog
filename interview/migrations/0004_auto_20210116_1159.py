# Generated by Django 3.1.5 on 2021-01-16 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0003_auto_20210116_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='candidate_remark',
            field=models.CharField(blank=True, max_length=135, verbose_name='應徵者訊息備註'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='degree',
            field=models.CharField(blank=True, choices=[('大學', '大學'), ('碩士', '碩士'), ('博士', '博士')], max_length=135, verbose_name='學歷'),
        ),
    ]
