# Generated by Django 3.2.8 on 2021-11-02 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_rename_article_tag_article_article_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlemaintag',
            old_name='article_tag',
            new_name='article_tags',
        ),
    ]
