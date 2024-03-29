# Generated by Django 4.2 on 2024-02-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("financial", "0002_payment_amount"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payment",
            options={"ordering": ("-updated_at",)},
        ),
        migrations.RenameField(
            model_name="payment",
            old_name="paid_at",
            new_name="created_at",
        ),
        migrations.RemoveField(
            model_name="payment",
            name="payment_method",
        ),
        migrations.AddField(
            model_name="payment",
            name="accept",
            field=models.CharField(
                choices=[("a", "Accept"), ("r", "Reject")], default="A", max_length=1
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
