# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-05 23:01
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkings', '0018_parking_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('created_at',
                 models.DateTimeField(
                     auto_now_add=True, verbose_name='time created')),
                ('modified_at',
                 models.DateTimeField(
                     auto_now=True, verbose_name='time modified')),
                ('external_id',
                 models.CharField(blank=True, max_length=50, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('_subjects', models.CharField(max_length=1000)),
                ('_areas', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('series', 'start_time', '-end_time', 'id'),
            },
        ),
        migrations.CreateModel(
            name='PermitSeries',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('created_at',
                 models.DateTimeField(
                     auto_now_add=True, verbose_name='time created')),
                ('modified_at',
                 models.DateTimeField(
                     auto_now=True, verbose_name='time modified')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created_at', 'id'),
            },
        ),
        migrations.AddField(
            model_name='permit',
            name='series',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to='parkings.PermitSeries'),
        ),
        migrations.AddIndex(
            model_name='permit',
            index=models.Index(
                fields=['series', 'start_time', '-end_time', 'id'],
                name='parkings_pe_series__804774_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='permit',
            unique_together=set([('series', 'external_id')]),
        ),
    ]
