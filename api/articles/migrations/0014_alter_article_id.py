# Generated by Django 3.2.5 on 2021-08-26 07:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_edition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.IntegerField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
