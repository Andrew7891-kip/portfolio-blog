# Generated by Django 3.0.5 on 2020-06-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_portfolio_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='photo',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]