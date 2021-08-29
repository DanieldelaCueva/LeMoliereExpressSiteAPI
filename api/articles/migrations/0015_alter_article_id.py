# Generated by Django 3.2.5 on 2021-08-26 07:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_alter_article_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.IntegerField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]