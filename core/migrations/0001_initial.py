# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 23:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('icon', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Frequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=15)),
                ('quant_days', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=25)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateTimeField()),
                ('type_operation', models.CharField(choices=[('IN', 'INCREASE'), ('OUT', 'DECREASE')], max_length=3)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=25)),
                ('movement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='core.Movement')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('limit_billing_monthly', models.DecimalField(decimal_places=2, max_digits=6)),
                ('categories', models.ManyToManyField(to='core.Category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_in', models.DateTimeField()),
                ('next_action', models.DateTimeField()),
                ('frequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Frequence')),
                ('movement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recurrence', to='core.Movement')),
            ],
        ),
        migrations.CreateModel(
            name='RequestCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('approved', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Tranfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='core.Profile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='core.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='movement',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
    ]
