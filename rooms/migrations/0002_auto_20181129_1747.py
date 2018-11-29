# Generated by Django 2.1.3 on 2018-11-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('HA', 'Horrow with actor'), ('HW', 'Horrow without actor'), ('PA', 'Puzzle with actor'), ('PW', 'Puzzle without actor'), ('CA', 'Comedy with actor'), ('CW', 'Comedy without actor'), ('PSA', 'Police-Spy with actor'), ('PSW', 'Police-Spy without actor'), ('KW', 'Kids Friendly')], default='CW', max_length=3),
        ),
        migrations.AlterField(
            model_name='room',
            name='duration',
            field=models.CharField(choices=[('60M', '60 Minutes'), ('70M', '70 Minutes'), ('80M', '80 Minutes'), ('90M', '90 Minutes'), ('90+M', '90+ Minutes')], default='60M', max_length=3),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo_main',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
