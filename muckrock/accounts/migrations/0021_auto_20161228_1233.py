# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-28 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_profile_preferred_proxy'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='machine_requests',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='machine_requests_abandoned',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='machine_requests_awaiting_ack',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='machine_requests_awaiting_appeal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='machine_requests_awaiting_response',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='machine_requests_denied',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='machine_requests_draft',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='machine_requests_fix_required',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='machine_requests_no_docs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='machine_requests_partial',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='machine_requests_payment_required',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='machine_requests_submitted',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='machine_requests_success',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]