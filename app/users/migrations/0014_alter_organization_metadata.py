# Generated by Django 4.0 on 2022-02-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_driver_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='metadata',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
