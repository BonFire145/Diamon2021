# Generated by Django 3.1.4 on 2021-11-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20211015_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='bloodinfo_origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param1', models.IntegerField()),
                ('param2', models.IntegerField()),
                ('param3', models.IntegerField()),
                ('param4', models.IntegerField()),
                ('param5', models.IntegerField()),
                ('param6', models.IntegerField()),
                ('param7', models.IntegerField()),
                ('param8', models.IntegerField()),
                ('param9', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='bloodinfo',
            name='param9',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Posting',
        ),
    ]
