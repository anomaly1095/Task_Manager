# Generated by Django 5.0.1 on 2024-01-22 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_end_time_alter_task_time_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, default=models.CharField(blank=True, default='task', max_length=30), max_length=255, null=True),
        ),
    ]
