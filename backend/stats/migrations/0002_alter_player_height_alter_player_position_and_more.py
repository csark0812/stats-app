# Generated by Django 4.2.3 on 2023-08-03 04:49

from django.db import migrations, models
import django.db.models.deletion
import stats.validators


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="height",
            field=models.CharField(
                max_length=20, validators=[stats.validators.validate_height]
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="position",
            field=models.CharField(
                choices=[
                    ("G", "Guard"),
                    ("F", "Forward"),
                    ("PG", "Point Guard"),
                    ("SG", "Shooting Guard"),
                    ("SF", "Small Forward"),
                    ("PF", "Power Forward"),
                    ("C", "Center"),
                ],
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="stats.team",
            ),
        ),
    ]
