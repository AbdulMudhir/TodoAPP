# Generated by Django 3.0.3 on 2020-04-15 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200415_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 21, 49, 18, 191325)),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='title',
            field=models.TextField(default=''),
        ),
    ]