# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0004_remove_activegoldstandards_last_changed'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='goldstandard',
            unique_together=set([('session_date', 'gen_court_house')]),
        ),
    ]
