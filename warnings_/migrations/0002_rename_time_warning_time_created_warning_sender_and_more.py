# Generated by Django 4.0.5 on 2022-07-26 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_rename_timestamp_admin_time_created_and_more'),
        ('warnings_', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warning',
            old_name='time',
            new_name='time_created',
        ),
        migrations.AddField(
            model_name='warning',
            name='sender',
            field=models.CharField(default='mr.hep_', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='warning',
            name='server',
            field=models.CharField(default='185.169.134.83:7777', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='warning',
            name='json',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='warning',
            name='sended_to',
            field=models.ManyToManyField(blank=True, null=True, related_name='sended_to', to='admins.admin'),
        ),
    ]
