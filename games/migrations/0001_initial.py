# Generated by Django 2.1.7 on 2019-02-19 06:33

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('bgg_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(blank=True, db_index=True, null=True)),
                ('owned', models.BooleanField(db_index=True, default=False)),
                ('wishlist', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('play_count', models.PositiveIntegerField(db_index=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('bgg_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('alt_name', django_extensions.db.fields.json.JSONField(default=list)),
                ('year', models.SmallIntegerField(blank=True, db_index=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('image_url', django_extensions.db.fields.json.JSONField(default=list)),
                ('video_url', django_extensions.db.fields.json.JSONField(default=list)),
                ('external_link', django_extensions.db.fields.json.JSONField(default=list)),
                ('min_players', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('max_players', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('min_players_rec', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('max_players_rec', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('min_players_best', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('max_players_best', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('min_age', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('max_age', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('min_age_rec', models.FloatField(blank=True, db_index=True, null=True)),
                ('max_age_rec', models.FloatField(blank=True, db_index=True, null=True)),
                ('min_time', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('max_time', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('cooperative', models.BooleanField(db_index=True, default=False)),
                ('compilation', models.BooleanField(db_index=True, default=False)),
                ('bgg_rank', models.PositiveIntegerField(blank=True, db_index=True, null=True)),
                ('num_votes', models.PositiveIntegerField(db_index=True, default=0)),
                ('avg_rating', models.FloatField(blank=True, db_index=True, null=True)),
                ('stddev_rating', models.FloatField(blank=True, db_index=True, null=True)),
                ('bayes_rating', models.FloatField(blank=True, db_index=True, null=True)),
                ('rec_rank', models.PositiveIntegerField(blank=True, db_index=True, null=True)),
                ('rec_rating', models.FloatField(blank=True, db_index=True, null=True)),
                ('rec_stars', models.FloatField(blank=True, db_index=True, null=True)),
                ('complexity', models.FloatField(blank=True, db_index=True, null=True)),
                ('language_dependency', models.FloatField(blank=True, db_index=True, null=True)),
                ('freebase_id', django_extensions.db.fields.json.JSONField(default=list)),
                ('wikidata_id', django_extensions.db.fields.json.JSONField(default=list)),
                ('wikipedia_id', django_extensions.db.fields.json.JSONField(default=list)),
                ('dbpedia_id', django_extensions.db.fields.json.JSONField(default=list)),
                ('luding_id', django_extensions.db.fields.json.JSONField(default=list)),
                ('spielen_id', django_extensions.db.fields.json.JSONField(default=list)),
                ('bga_id', django_extensions.db.fields.json.JSONField(default=list)),
            ],
            options={
                'ordering': ('-rec_rating', '-bayes_rating', '-avg_rating'),
            },
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('bgg_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('bgg_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('bgg_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('games', models.ManyToManyField(blank=True, through='games.Collection', to='games.Game')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='game',
            name='artist',
            field=models.ManyToManyField(blank=True, related_name='artist_of', to='games.Person'),
        ),
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='games', to='games.Category'),
        ),
        migrations.AddField(
            model_name='game',
            name='compilation_of',
            field=models.ManyToManyField(blank=True, related_name='contained_in', to='games.Game'),
        ),
        migrations.AddField(
            model_name='game',
            name='designer',
            field=models.ManyToManyField(blank=True, related_name='designer_of', to='games.Person'),
        ),
        migrations.AddField(
            model_name='game',
            name='game_type',
            field=models.ManyToManyField(blank=True, related_name='games', to='games.GameType'),
        ),
        migrations.AddField(
            model_name='game',
            name='implements',
            field=models.ManyToManyField(blank=True, related_name='implemented_by', to='games.Game'),
        ),
        migrations.AddField(
            model_name='game',
            name='integrates_with',
            field=models.ManyToManyField(blank=True, related_name='_game_integrates_with_+', to='games.Game'),
        ),
        migrations.AddField(
            model_name='game',
            name='mechanic',
            field=models.ManyToManyField(blank=True, related_name='games', to='games.Mechanic'),
        ),
        migrations.AddField(
            model_name='collection',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.User'),
        ),
        migrations.AddIndex(
            model_name='game',
            index=models.Index(fields=['-rec_rating', '-bayes_rating', '-avg_rating'], name='games_game_rec_rat_3cf101_idx'),
        ),
        migrations.AddIndex(
            model_name='collection',
            index=models.Index(fields=['user', 'owned'], name='games_colle_user_id_b77c0a_idx'),
        ),
    ]
