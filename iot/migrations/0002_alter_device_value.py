# Generated by Django 4.2.1 on 2023-05-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='value',
            field=models.IntegerField(),
        ),
    ]
