# Generated by Django 3.0.5 on 2020-07-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20200619_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='p1',
            field=models.ImageField(null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='p2',
            field=models.ImageField(null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='p3',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]