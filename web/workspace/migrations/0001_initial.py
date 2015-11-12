# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Execution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'queue', max_length=20)),
                ('executor', models.CharField(max_length=50)),
                ('starttime', models.DateTimeField(auto_now_add=True)),
                ('endtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('starttime', models.DateTimeField(auto_now_add=True)),
                ('endtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkSpace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('rootlocation', models.CharField(max_length=755)),
                ('createat', models.DateTimeField(auto_now_add=True)),
                ('updateat', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='execution',
            name='testlog',
            field=models.OneToOneField(to='workspace.TestLog'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='execution',
            name='workspace',
            field=models.ForeignKey(to='workspace.WorkSpace'),
            preserve_default=True,
        ),
    ]
