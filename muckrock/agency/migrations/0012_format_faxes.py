# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-23 21:18
from __future__ import unicode_literals

from django.db import migrations

import phonenumbers

# XXX move this in front of other migrations

def format_faxes(apps, schema_editor):
    """Normalize faxes"""
    Agency = apps.get_model('agency', 'Agency')
    for agency in Agency.objects.exclude(fax=''):
        try:
            if agency.fax == 'n/a':
                agency.fax = ''
            elif agency.fax.strip() == '':
                agency.fax = ''
            elif agency.fax.endswith('@fax2.faxaway.com'):
                number = phonenumbers.parse(agency.fax.split('@')[0], 'US')
                agency.fax = phonenumbers.format_number(
                        number,
                        phonenumbers.PhoneNumberFormat.NATIONAL)
            else:
                number = phonenumbers.parse(agency.fax, 'US')
                agency.fax = phonenumbers.format_number(
                        number,
                        phonenumbers.PhoneNumberFormat.NATIONAL)
            agency.save()
        except phonenumbers.NumberParseException:
            print 'Parse Error: "{}"'.format(agency.fax)


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0011_change_agencyprofile_contacttype'),
    ]

    operations = [
        migrations.RunPython(format_faxes, lambda a, s: None),
    ]