# Generated by Django 5.0.3 on 2024-03-31 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whistleblower_site', '0007_remove_report_follow_up_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='file',
        ),
        migrations.CreateModel(
            name='ReportFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='org-report-uploaded-files/')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_files', to='whistleblower_site.report')),
            ],
        ),
    ]
