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
                ('workspace', models.IntegerField()),
                ('deleted', models.BooleanField(default=False)),
                ('executionLock', models.BooleanField(default=False)),
                ('feature_key', models.CharField(default=b'default_key', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('prefix', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=1023)),
                ('url', models.URLField(default=b'')),
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
                ('step_sequence', models.TextField()),
                ('deleted', models.BooleanField(default=False)),
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
                ('description_with_agrs', models.CharField(max_length=255)),
                ('function', models.CharField(max_length=255)),
                ('module', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('argnumbers', models.IntegerField()),
                ('varlist', models.CharField(max_length=255)),
                ('deleted', models.BooleanField(default=False)),
                ('action_type', models.CharField(default=b'Then', max_length=20)),
                ('co_variables', models.CharField(max_length=255)),
                ('scenario', models.ForeignKey(to='auto.Scenario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1023)),
                ('parent_id', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
                ('project', models.ForeignKey(to='auto.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
