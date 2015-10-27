# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('function', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('module', models.CharField(max_length=255)),
                ('location', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
