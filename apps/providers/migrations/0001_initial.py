# Generated by Django 3.2.13 on 2022-06-02 22:05

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3)),
                ('email', models.EmailField(max_length=254)),
                ('language', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=200)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0.0)),
                ('polygon', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='providers.provider')),
            ],
        ),
    ]
