# Generated by Django 4.2 on 2024-02-23 08:13

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0014_alter_gallery_image_alter_gallery_video_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                blank=True,
                default=None,
                editable=False,
                max_length=250,
                null=True,
                populate_from="name",
                unique=True,
            ),
        ),
    ]
