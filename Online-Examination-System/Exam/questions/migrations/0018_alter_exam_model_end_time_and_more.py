# Generated by Django 4.2.5 on 2024-03-08 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_alter_exam_model_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 8, 17, 41, 35, 590533)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 8, 17, 41, 35, 590533)),
        ),
    ]