# Generated by Django 3.2.8 on 2021-10-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.TextField(),
        ),
    ]
