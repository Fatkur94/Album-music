# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('artist', models.CharField(max_length=50)),
                ('album_title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=100)),
                ('album_logo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('file_type', models.CharField(max_length=10)),
                ('song_title', models.CharField(max_length=50)),
                ('album', models.ForeignKey(to='music.Album')),
            ],
        ),
    ]
