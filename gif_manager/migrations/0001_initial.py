# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('latest_post', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Gif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gif_manager.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='gif',
            name='tag',
            field=models.ManyToManyField(to='gif_manager.Tag'),
        ),
    ]
