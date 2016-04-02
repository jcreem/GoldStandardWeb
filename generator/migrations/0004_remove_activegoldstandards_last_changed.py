# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_auto_20160401_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activegoldstandards',
            name='last_changed',
        ),
    ]
