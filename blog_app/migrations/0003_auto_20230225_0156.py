# Generated by Django 3.2.8 on 2023-02-25 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='end_date',
            field=models.DateField(null=True, verbose_name=datetime.date.today),
        ),
        migrations.AddField(
            model_name='post',
            name='start_date',
            field=models.DateField(null=True, verbose_name=datetime.date.today),
        ),
    ]