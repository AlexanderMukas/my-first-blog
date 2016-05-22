# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mid_name', models.CharField(max_length=100)),
                ('date_enter', models.DateField(null=True, blank=True)),
                ('date_dismis', models.DateField(null=True, blank=True)),
                ('num_pass', models.CharField(max_length=8)),
                ('inn', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]
