# Generated by Django 4.1.3 on 2023-10-05 19:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio_app", "0023_rename_type_id_biography_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="biography",
            old_name="type",
            new_name="biography_type",
        ),
    ]
