# Generated by Django 4.1.6 on 2023-02-09 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_date_conclusion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_conclusion',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 9, 17, 35, 59, 519166, tzinfo=datetime.timezone.utc), verbose_name='Data de conclusão'),
        ),
    ]
