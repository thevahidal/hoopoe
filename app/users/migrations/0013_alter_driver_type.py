# Generated by Django 4.0 on 2021-12-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_rename_username_driver_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='type',
            field=models.IntegerField(choices=[(0, 'EMAIL'), (1, 'TELEGRAM')], default=0),
        ),
    ]
