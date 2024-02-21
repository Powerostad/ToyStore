# Generated by Django 4.2 on 2024-02-21 07:10

import autoslug.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_post_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                always_update=True,
                editable=True,
                max_length=250,
                null=True,
                populate_from="name",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="published",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 21, 7, 10, 10, 117474, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Published",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                always_update=True,
                editable=True,
                max_length=250,
                null=True,
                populate_from="title",
                unique_for_date="published",
            ),
        ),
    ]
