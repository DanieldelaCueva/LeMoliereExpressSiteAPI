# Generated by Django 3.2.5 on 2021-08-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_auto_20210724_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='is_coordinator',
            field=models.BooleanField(default=False),
        ),
    ]