# Generated by Django 4.1 on 2023-08-21 14:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("people", "0007_alter_alumni_year_alter_btech_year_alter_mtech_year_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="faculty",
            name="subtitle",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
