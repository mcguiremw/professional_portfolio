# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('Exp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blog.Experience')),
                ('employer', models.CharField(max_length=80)),
            ],
            bases=('blog.experience',),
        ),
    ]
