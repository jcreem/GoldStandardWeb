# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0006_auto_20160402_0901'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='goldstandard',
            unique_together=set([]),
        ),
    ]
