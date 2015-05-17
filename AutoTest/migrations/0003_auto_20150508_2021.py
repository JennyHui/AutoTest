# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AutoTest', '0002_auto_20150508_1905'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
