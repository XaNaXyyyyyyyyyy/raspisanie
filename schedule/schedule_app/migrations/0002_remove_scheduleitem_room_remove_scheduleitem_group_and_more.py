# Generated by Django 5.1.1 on 2024-09-07 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleitem',
            name='room',
        ),
        migrations.RemoveField(
            model_name='scheduleitem',
            name='group',
        ),
        migrations.RemoveField(
            model_name='scheduleitem',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='scheduleitem',
            name='teacher',
        ),
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule_app.group')),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='ScheduleItem',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
