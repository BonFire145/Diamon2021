# Generated by Django 3.1.4 on 2021-10-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_bloodinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodinfo',
            name='param9',
            field=models.IntegerField(max_length=20),
        ),
    ]