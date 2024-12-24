# Generated by Django 4.2.4 on 2024-12-24 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0012_taskresult_date_started'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='taskresult',
            index=models.Index(fields=['periodic_task_name'], name='django_cele_periodi_0a0f9e_idx'),
        ),
        migrations.AddIndex(
            model_name='taskresult',
            index=models.Index(fields=['task_args'], name='django_cele_task_ar_0b3b3e_idx'),
        ),
        migrations.AddIndex(
            model_name='taskresult',
            index=models.Index(fields=['task_kwargs'], name='django_cele_task_kw_0b3b3e_idx'),
        ),
    ]
