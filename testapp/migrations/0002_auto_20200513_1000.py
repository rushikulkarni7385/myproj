# Generated by Django 3.0.5 on 2020-05-13 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banglore_jobs',
            name='Posted_date',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hyd_jobs',
            name='Posted_date',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pune_jobs',
            name='Posted_date',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
