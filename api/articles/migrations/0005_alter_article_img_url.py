# Generated by Django 3.2.5 on 2021-07-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_validated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img_url',
            field=models.TextField(),
        ),
    ]
