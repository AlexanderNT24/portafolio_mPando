# Generated by Django 3.2.8 on 2023-04-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0018_exhibition_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
