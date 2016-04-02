# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0008_auto_20160402_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goldstandard',
            name='session_date',
            field=models.DateField(verbose_name=b'session date'),
            preserve_default=True,
        ),
    ]
