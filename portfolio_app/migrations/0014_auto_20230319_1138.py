# Generated by Django 3.2.8 on 2023-03-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0013_auto_20230318_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='image',
            field=models.ImageField(upload_to='portfolio_app/images'),
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exhibition_view',
            name='image',
            field=models.ImageField(upload_to='portfolio_app/images'),
        ),
    ]