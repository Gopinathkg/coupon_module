# Generated by Django 3.0.2 on 2020-01-10 15:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userregistration',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reference', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
                ('city', models.CharField(blank=True, choices=[('ch', 'Chennai'), ('VE', 'Vellore'), ('BE', 'Banglore')], max_length=2)),
                ('reference_coupon', models.CharField(max_length=7, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reference_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coupon.UserRegistration')),
            ],
        ),
    ]
