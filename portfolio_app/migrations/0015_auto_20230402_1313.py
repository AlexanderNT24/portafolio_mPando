# Generated by Django 3.2.8 on 2023-04-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0014_auto_20230319_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition_view',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='exhibition_view',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
