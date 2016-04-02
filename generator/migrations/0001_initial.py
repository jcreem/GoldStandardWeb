# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoldStandard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_date', models.DateTimeField(verbose_name=b'session date')),
                ('google_sheet_url', models.URLField(verbose_name=b'google sheet url')),
                ('gen_court_house', models.CharField(default=b'Hou', max_length=3, choices=[(b'Hou', b'House'), (b'Sen', b'Senate')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
