# Generated by Django 2.1.3 on 2018-11-23 15:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('difficulty', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/%d/%m/%Y/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%d/%m/%Y/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%d/%m/%Y/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%d/%m/%Y/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%d/%m/%Y/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%d/%m/%Y/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%d/%m/%Y/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='companies.Company')),
            ],
        ),
    ]
