# Generated by Django 3.2 on 2021-04-25 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playapp', '0002_play_download'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='download',
            field=models.FileField(upload_to='media'),
        ),
    ]
