# Generated by Django 3.0.5 on 2020-06-19 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200618_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='photo',
        ),
    ]
