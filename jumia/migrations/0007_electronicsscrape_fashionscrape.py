# Generated by Django 3.0.1 on 2020-01-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumia', '0006_auto_20200127_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectronicsScrape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField()),
                ('product', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=10)),
                ('old_price', models.CharField(max_length=10)),
                ('product_url', models.URLField(max_length=300, unique=True)),
                ('img_url', models.URLField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='FashionScrape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField()),
                ('product', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=10)),
                ('old_price', models.CharField(max_length=10)),
                ('product_url', models.URLField(max_length=300, unique=True)),
                ('img_url', models.URLField(max_length=300)),
            ],
        ),
    ]
