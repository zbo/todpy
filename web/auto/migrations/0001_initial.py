# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('module', models.CharField(max_length=255)),
                ('location', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('feature', models.ForeignKey(to='auto.Feature')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('function', models.CharField(max_length=255)),
                ('module', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('argnumbers', models.IntegerField()),
                ('varlist', models.CharField(max_length=255)),
                ('scenario', models.ForeignKey(to='auto.Scenario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
