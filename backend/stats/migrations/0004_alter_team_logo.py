# Generated by Django 4.2.3 on 2023-08-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0003_alter_league_overtime_length_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="team_logos/"),
        ),
    ]