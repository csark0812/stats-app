# Generated by Django 4.2.3 on 2023-08-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0002_alter_league_period_length"),
    ]

    operations = [
        migrations.AlterField(
            model_name="league",
            name="overtime_length",
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name="league",
            name="shot_clock_length",
            field=models.DurationField(),
        ),
    ]
