# Generated by Django 4.2.3 on 2023-07-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producphoto',
            name='slug',
            field=models.SlugField(default=22, max_length=200),
            preserve_default=False,
        ),
    ]