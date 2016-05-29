# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20160529_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employees',
            options={'verbose_name': 'Работники'},
        ),
        migrations.AlterField(
            model_name='employees',
            name='date_dismis',
            field=models.DateField(verbose_name='дата_увольнения', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='date_enter',
            field=models.DateField(verbose_name='дата_принятия', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='inn',
            field=models.CharField(max_length=10, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='mid_name',
            field=models.CharField(max_length=100, verbose_name='отчество'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='num_pass',
            field=models.CharField(max_length=8, verbose_name='№паспорта'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='телефон'),
        ),
    ]
