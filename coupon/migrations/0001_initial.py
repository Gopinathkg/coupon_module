# Generated by Django 3.0.2 on 2020-01-10 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
                ('city', models.CharField(blank=True, choices=[('ch', 'Chennai'), ('VE', 'Vellore'), ('BE', 'Banglore')], max_length=2)),
                ('coupon', models.CharField(max_length=7, null=True, unique=True)),
            ],
        ),
    ]