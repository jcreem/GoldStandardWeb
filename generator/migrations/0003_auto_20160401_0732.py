# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_activegoldstandards'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activegoldstandards',
            old_name='GoldStandard',
            new_name='goldstandard',
        ),
        migrations.AddField(
            model_name='activegoldstandards',
            name='last_changed',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 11, 32, 5, 804342, tzinfo=utc), verbose_name=b'Last Changed Date'),
            preserve_default=False,
        ),
    ]
