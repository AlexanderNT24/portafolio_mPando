# Generated by Django 3.2.8 on 2023-02-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0010_alter_exhibition_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='description',
            field=models.TextField(max_length=10000),
        ),
    ]