# Generated by Django 4.2.5 on 2024-03-08 17:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0019_alter_exam_model_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 8, 19, 35, 13, 439556)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='professor',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Professor'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 8, 19, 35, 13, 439556)),
        ),
    ]
