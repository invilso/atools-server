# Generated by Django 4.0.5 on 2022-07-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_rename_timestamp_admin_time_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='last_online',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='spectate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]