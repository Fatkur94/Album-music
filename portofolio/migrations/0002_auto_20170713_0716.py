# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import portofolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_portofolio',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post_portofolio',
            name='image',
            field=models.ImageField(height_field='height_field', width_field='width_field', blank=True, null=True, upload_to=portofolio.models.image_location),
        ),
        migrations.AddField(
            model_name='post_portofolio',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
