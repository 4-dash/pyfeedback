# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0030_auto_20170108_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='veranstaltung',
            name='primaerdozent',
            field=models.ForeignKey(blank=True, help_text='Die Person, die am Anschreiben steht', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primaerdozent', to='feedback.Person'),
        ),
    ]