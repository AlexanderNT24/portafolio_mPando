# Generated by Django 4.1.3 on 2023-04-02 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0016_alter_exhibition_city_alter_exhibition_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exhibition",
            name="date",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="exhibition",
            name="ubication",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
