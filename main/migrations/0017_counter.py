# Generated by Django 5.0.2 on 2024-02-19 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Counter',
                'verbose_name_plural': 'Counters',
            },
        ),
    ]
