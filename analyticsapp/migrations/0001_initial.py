# Generated by Django 3.0.6 on 2020-08-26 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
