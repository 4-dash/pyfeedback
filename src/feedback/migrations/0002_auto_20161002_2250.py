# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-02 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ergebnis2008',
            name='veranstaltung',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='feedback.Veranstaltung'),
        ),
        migrations.AlterField(
            model_name='ergebnis2009',
            name='veranstaltung',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='feedback.Veranstaltung'),
        ),
        migrations.AlterField(
            model_name='ergebnis2012',
            name='veranstaltung',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='feedback.Veranstaltung'),
        ),
        migrations.AlterField(
            model_name='ergebnis2016',
            name='veranstaltung',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='feedback.Veranstaltung'),
        ),
    ]
