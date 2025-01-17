# Generated by Django 5.1.3 on 2024-12-14 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_feedbacks'),
    ]

    operations = [
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txn_id', models.CharField(max_length=30)),
                ('farmerName', models.CharField(max_length=50)),
                ('industryName', models.CharField(max_length=50)),
                ('materialType', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('ss', models.FileField(upload_to='')),
            ],
        ),
    ]
