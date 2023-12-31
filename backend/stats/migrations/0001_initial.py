# Generated by Django 4.2.3 on 2023-08-17 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Division",
            fields=[
                ("division_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="DivisionSeason",
            fields=[
                (
                    "division_season_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "division",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seasons",
                        to="stats.division",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                ("game_id", models.AutoField(primary_key=True, serialize=False)),
                ("location", models.CharField(max_length=50)),
                ("date_time", models.DateTimeField()),
                ("counts_towards_record", models.BooleanField()),
                ("time_on_clock", models.DurationField()),
                ("period", models.PositiveIntegerField()),
                ("away_s30_timeouts_taken", models.PositiveIntegerField()),
                ("home_s30_timeouts_taken", models.PositiveIntegerField()),
                ("away_full_timeouts_taken", models.PositiveIntegerField()),
                ("home_full_timeouts_taken", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="League",
            fields=[
                ("league_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("foul_out", models.PositiveIntegerField()),
                ("bonus_foul_amt", models.PositiveIntegerField()),
                ("dbl_bonus_foul_amt", models.PositiveIntegerField()),
                ("full_timeouts", models.PositiveIntegerField()),
                ("s30_timeouts", models.PositiveIntegerField()),
                ("possession_arrow", models.BooleanField(default=True)),
                ("period_length", models.PositiveIntegerField()),
                ("period_amt", models.PositiveIntegerField()),
                ("shot_clock_length", models.PositiveIntegerField()),
                ("overtime_length", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                ("player_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("height", models.DecimalField(decimal_places=2, max_digits=4)),
                (
                    "league",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="players",
                        to="stats.league",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PlayerSeason",
            fields=[
                (
                    "player_season_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("jersey_number", models.PositiveIntegerField()),
                (
                    "position",
                    models.CharField(
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
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seasons",
                        to="stats.player",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Season",
            fields=[
                ("season_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "league",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seasons",
                        to="stats.league",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                ("team_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("abbreviation", models.CharField(max_length=10)),
                ("logo", models.ImageField(upload_to="team_logos/")),
                (
                    "league",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teams",
                        to="stats.league",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TeamSeason",
            fields=[
                ("team_season_id", models.AutoField(primary_key=True, serialize=False)),
                ("head_coach", models.CharField(max_length=50)),
                (
                    "division",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="teams",
                        to="stats.divisionseason",
                    ),
                ),
                (
                    "season",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teams",
                        to="stats.season",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seasons",
                        to="stats.team",
                    ),
                ),
            ],
            options={
                "unique_together": {("team", "season")},
            },
        ),
        migrations.CreateModel(
            name="StatLine",
            fields=[
                ("statline_id", models.AutoField(primary_key=True, serialize=False)),
                ("mins", models.DurationField()),
                ("fg2m", models.PositiveIntegerField()),
                ("fg2a", models.PositiveIntegerField()),
                ("fg3m", models.PositiveIntegerField()),
                ("fg3a", models.PositiveIntegerField()),
                ("ftm", models.PositiveIntegerField()),
                ("fta", models.PositiveIntegerField()),
                ("oreb", models.PositiveIntegerField()),
                ("dreb", models.PositiveIntegerField()),
                ("ast", models.PositiveIntegerField()),
                ("stl", models.PositiveIntegerField()),
                ("blk", models.PositiveIntegerField()),
                ("tov", models.PositiveIntegerField()),
                ("pf", models.PositiveIntegerField()),
                ("tf", models.PositiveIntegerField()),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="statsheet",
                        to="stats.game",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="statlines",
                        to="stats.playerseason",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="statsheet",
                        to="stats.teamseason",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RecordedStat",
            fields=[
                ("stat_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "stat",
                    models.CharField(
                        choices=[
                            ("fg2m", "Two-point Field Goal Made"),
                            ("fg2a", "Two-point Field Goal Attempted"),
                            ("fg3m", "Three-Point Field Goal Made"),
                            ("fg3a", "Three-Point Field Goal Attempted"),
                            ("ftm", "Free Throw Made"),
                            ("fta", "Free Throw Attempted"),
                            ("oreb", "Offensive Rebound"),
                            ("dreb", "Defensive Rebound"),
                            ("ast", "Assist"),
                            ("stl", "Steal"),
                            ("blk", "Block"),
                            ("tov", "Turnover"),
                            ("pf", "Personal Foul"),
                            ("tf", "Technical Foul"),
                            ("sub_in", "Substitute In"),
                            ("sub_out", "Substitute Out"),
                            ("period_start", "Start of Period"),
                            ("period_end", "End of Period"),
                        ],
                        max_length=12,
                    ),
                ),
                ("period", models.PositiveIntegerField()),
                ("timestamp", models.DurationField()),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="statistics",
                        to="stats.game",
                    ),
                ),
                (
                    "linked_statID",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stats.recordedstat",
                    ),
                ),
                (
                    "statline",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="statistics",
                        to="stats.statline",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="playerseason",
            name="season",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="players",
                to="stats.season",
            ),
        ),
        migrations.AddField(
            model_name="playerseason",
            name="team_season",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="players",
                to="stats.teamseason",
            ),
        ),
        migrations.AddField(
            model_name="game",
            name="away_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="away_games",
                to="stats.teamseason",
            ),
        ),
        migrations.AddField(
            model_name="game",
            name="home_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="home_games",
                to="stats.teamseason",
            ),
        ),
        migrations.AddField(
            model_name="divisionseason",
            name="season",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="divisions",
                to="stats.season",
            ),
        ),
        migrations.AddField(
            model_name="division",
            name="league",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="divisions",
                to="stats.league",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="playerseason",
            unique_together={("player", "season")},
        ),
        migrations.AlterUniqueTogether(
            name="divisionseason",
            unique_together={("division", "season")},
        ),
    ]
