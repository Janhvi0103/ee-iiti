# Generated by Django 4.1 on 2023-08-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("people", "0009_alter_faculty_subtitle"),
    ]

    operations = [
        migrations.AddField(
            model_name="faculty",
            name="phone",
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
