# Generated by Django 5.0 on 2024-01-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDigesto', '0004_alter_digesto_fecha_vigencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digesto',
            name='fecha_vigencia',
            field=models.DateField(),
        ),
    ]
