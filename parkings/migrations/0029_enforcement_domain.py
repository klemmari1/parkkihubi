# Generated by Django 2.2.8 on 2020-01-15 13:05

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parkings', '0028_digital_disc_changes'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnforcementDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='time modified')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(
                    srid=3879, verbose_name='geometry', null=True
                )),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Enforcer',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='time modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('enforced_domain', models.ForeignKey(
                    help_text='The enforcement domain enforced by this enforcer',
                    on_delete=django.db.models.deletion.PROTECT,
                    to='parkings.EnforcementDomain',
                    verbose_name='enforced domain')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT,
                                              to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'enforcer',
                'verbose_name_plural': 'enforcers',
            },
        ),
        migrations.AddField(
            model_name='paymentzone',
            name='code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='permitseries',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    verbose_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='paymentzone',
            name='number',
            field=models.IntegerField(verbose_name='zone number'),
        ),
        migrations.AlterField(
            model_name='permitarea',
            name='identifier',
            field=models.CharField(max_length=10, verbose_name='identifier'),
        ),
        migrations.AddField(
            model_name='parking',
            name='domain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='parkings', to='parkings.EnforcementDomain'),
        ),
        migrations.AddField(
            model_name='parkingarea',
            name='domain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='parking_areas', to='parkings.EnforcementDomain'),
        ),
        migrations.AddField(
            model_name='parkingterminal',
            name='domain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='parking_terminals', to='parkings.EnforcementDomain'),
        ),
        migrations.AddField(
            model_name='paymentzone',
            name='domain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='payment_zones', to='parkings.EnforcementDomain'),
        ),
        migrations.AddField(
            model_name='permit',
            name='domain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='permits', to='parkings.EnforcementDomain'),
        ),
        migrations.AddField(
            model_name='permitarea',
            name='domain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='permit_areas', to='parkings.EnforcementDomain'),
        ),
        migrations.AddField(
            model_name='permitarea',
            name='permitted_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    verbose_name='permitted_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='permitarea',
            unique_together={('domain', 'identifier')},
        ),
        migrations.AlterModelOptions(
            name='paymentzone',
            options={'ordering': ('domain', 'code')},
        ),
    ]
