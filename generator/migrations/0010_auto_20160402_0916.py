# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0009_auto_20160402_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activegoldstandard',
            name='goldstandard',
            field=models.OneToOneField(to='generator.GoldStandard'),
            preserve_default=True,
        ),
    ]
