# Generated by Django 5.1.6 on 2025-03-06 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assistances', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assistance',
            options={'ordering': ('created_at',), 'verbose_name': 'assistance', 'verbose_name_plural': 'assistances'},
        ),
        migrations.RenameField(
            model_name='assistance',
            old_name='date_time',
            new_name='created_at',
        ),
    ]
