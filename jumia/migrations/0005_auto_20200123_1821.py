# Generated by Django 3.0.1 on 2020-01-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumia', '0004_auto_20200123_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='androidscrape',
            name='percent',
            field=models.IntegerField(),
        ),
    ]
