# Generated by Django 5.1.3 on 2024-12-06 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_industryrequirement_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerrequest',
            name='status',
            field=models.CharField(default=str, max_length=20),
            preserve_default=False,
        ),
    ]