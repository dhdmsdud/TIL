# Generated by Django 3.1.5 on 2021-01-28 02:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bbsApp', '0002_bbs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='regdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 2, 8, 2, 235934, tzinfo=utc)),
        ),
    ]
