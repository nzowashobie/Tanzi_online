# Generated by Django 4.2.5 on 2024-03-15 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0021_alter_exam_model_end_time_alter_exam_model_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 12, 34, 21, 256554)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 12, 34, 21, 256554)),
        ),
    ]
