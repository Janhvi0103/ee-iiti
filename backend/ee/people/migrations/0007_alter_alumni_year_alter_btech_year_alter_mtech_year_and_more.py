# Generated by Django 4.1.5 on 2023-08-08 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0006_alter_alumni_image_alter_btech_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alumni",
            name="year",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="btech",
            name="year",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="mtech",
            name="year",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="phd",
            name="year",
            field=models.IntegerField(),
        ),
    ]