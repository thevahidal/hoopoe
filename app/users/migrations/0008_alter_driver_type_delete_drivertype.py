# Generated by Django 4.0 on 2021-12-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_drivertype_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='type',
            field=models.IntegerField(choices=[(0, 'EMAIL')], default=0),
        ),
        migrations.DeleteModel(
            name='DriverType',
        ),
    ]