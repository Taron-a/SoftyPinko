# Generated by Django 5.0.2 on 2024-02-19 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_pricing_plans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing_plans',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
