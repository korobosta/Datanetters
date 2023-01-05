# Generated by Django 3.1.1 on 2020-09-16 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analyticsapp', '0005_auto_20200830_1403'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='datamining',
            table='data_mining',
        ),
        migrations.AlterModelTable(
            name='datavisualization',
            table='data_visualization',
        ),
        migrations.CreateModel(
            name='Dbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_name', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'dbs',
            },
        ),
        migrations.CreateModel(
            name='DataFileStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='media/data_file_storage/')),
                ('date_created', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'data_file_storage',
            },
        ),
    ]