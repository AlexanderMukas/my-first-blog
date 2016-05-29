# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='first_name',
            field=models.CharField(verbose_name='фамилия', max_length=100),
        ),
    ]
