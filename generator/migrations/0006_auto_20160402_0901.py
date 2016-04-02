# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0005_auto_20160402_0900'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActiveGoldStandards',
            new_name='ActiveGoldStandard',
        ),
    ]
