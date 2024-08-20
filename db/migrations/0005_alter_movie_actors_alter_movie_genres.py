# Generated by Django 4.0.2 on 2024-08-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_rename_actor_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='db.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='db.Genre'),
        ),
    ]
