# Generated by Django 2.2.12 on 2020-06-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkings', '0038_archived_parking'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivedparking',
            name='sanitized_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='time sanitized'),
        ),
    ]
