# Generated by Django 5.0.1 on 2024-02-02 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car_info_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
                ('fuel_efficiency', models.IntegerField()),
                ('battery_capacity', models.IntegerField()),
            ],
        ),
    ]