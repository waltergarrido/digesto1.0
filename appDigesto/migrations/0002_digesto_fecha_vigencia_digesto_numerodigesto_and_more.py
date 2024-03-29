# Generated by Django 5.0 on 2024-01-04 21:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDigesto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='digesto',
            name='fecha_vigencia',
            field=models.DateField(default=datetime.datetime(2024, 1, 4, 21, 48, 3, 360740, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='digesto',
            name='numeroDigesto',
            field=models.TextField(default=12, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='digesto',
            name='archivo',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
