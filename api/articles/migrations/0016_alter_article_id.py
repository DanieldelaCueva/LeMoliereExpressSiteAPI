# Generated by Django 3.2.5 on 2021-08-26 07:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_alter_article_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=264, primary_key=True, serialize=False, unique=True),
        ),
    ]