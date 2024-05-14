# Generated by Django 4.2.5 on 2024-02-25 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_alter_exam_model_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='subjects',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 25, 15, 14, 41, 37351)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 25, 15, 14, 41, 37351)),
        ),
    ]