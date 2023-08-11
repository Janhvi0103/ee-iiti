# Generated by Django 4.1.5 on 2023-04-04 15:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="events",
            name="link",
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]