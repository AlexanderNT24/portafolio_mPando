# Generated by Django 4.1.3 on 2023-04-02 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0015_auto_20230402_1313"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exhibition",
            name="city",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="exhibition",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
    ]