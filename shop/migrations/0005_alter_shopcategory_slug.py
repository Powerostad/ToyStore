# Generated by Django 4.2 on 2024-02-21 07:35

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0004_alter_shopcategory_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopcategory",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                blank=True,
                default=None,
                editable=False,
                max_length=250,
                null=True,
                populate_from="name",
            ),
        ),
    ]