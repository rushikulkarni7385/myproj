# Generated by Django 3.0.5 on 2020-05-13 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banglore_Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=64)),
                ('Job_Title', models.CharField(max_length=64)),
                ('Experience', models.CharField(max_length=64)),
                ('Location', models.CharField(max_length=64)),
                ('Salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hyd_Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=64)),
                ('Job_Title', models.CharField(max_length=64)),
                ('Experience', models.CharField(max_length=64)),
                ('Location', models.CharField(max_length=64)),
                ('Salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pune_Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=64)),
                ('Job_Title', models.CharField(max_length=64)),
                ('Experience', models.CharField(max_length=64)),
                ('Location', models.CharField(max_length=64)),
                ('Salary', models.IntegerField()),
            ],
        ),
    ]
