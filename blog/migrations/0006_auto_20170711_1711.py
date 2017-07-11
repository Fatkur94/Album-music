# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170711_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='catergory',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(verbose_name='Category', to='blog.Category', null=True, blank=True),
        ),
    ]
