# Generated by Django 4.2 on 2024-02-25 05:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("financial", "0006_remove_payment_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="accept",
        ),
        migrations.AddField(
            model_name="payment",
            name="is_paid",
            field=models.BooleanField(default=False),
        ),
    ]