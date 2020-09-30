# Generated by Django 3.1 on 2020-09-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRSTNAME', models.CharField(max_length=50)),
                ('LASTNAME', models.CharField(max_length=50)),
                ('ADDRESS', models.CharField(max_length=50)),
                ('AGE', models.IntegerField()),
                ('DOB', models.DateField()),
                ('BRANCH', models.CharField(max_length=50)),
                ('PHONENO', models.IntegerField()),
                ('EMAIL', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Bankform',
                'verbose_name_plural': 'Bankforms',
            },
        ),
    ]
