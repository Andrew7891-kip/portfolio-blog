# Generated by Django 3.0.5 on 2020-06-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200618_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='photo',
            field=models.ImageField(upload_to='img'),
        ),
    ]
