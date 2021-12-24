# Generated by Django 4.0 on 2021-12-24 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_driver_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='username',
            field=models.CharField(max_length=128),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='recipient',
            unique_together={('organization', 'username')},
        ),
    ]