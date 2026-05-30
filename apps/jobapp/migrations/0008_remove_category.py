# Generated manually after removing job categories.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0007_alter_job_experience_level_alter_job_work_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
