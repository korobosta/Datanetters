# Generated by Django 3.0.6 on 2020-08-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyticsapp', '0002_datamining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamining',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='datamining',
            name='file',
            field=models.FileField(upload_to='../media/data_mining/'),
        ),
        migrations.AlterModelTable(
            name='datamining',
            table=None,
        ),
    ]
