# Generated by Django 3.2.5 on 2021-08-21 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_rename_img_rel_url_article_img_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='creator',
        ),
    ]