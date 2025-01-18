# Generated by Django 5.1.3 on 2024-12-15 11:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_transactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='farmerrequest',
            unique_together={('farmerName', 'industryName', 'materialType')},
        ),
    ]
