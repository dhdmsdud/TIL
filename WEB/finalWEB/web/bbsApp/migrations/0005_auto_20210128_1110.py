# Generated by Django 3.1.5 on 2021-01-28 02:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bbsApp', '0004_auto_20210128_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='regdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]