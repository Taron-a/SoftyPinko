# Generated by Django 5.0.2 on 2024-02-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='media')),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Feature Item',
                'verbose_name_plural': 'Feature Items',
            },
        ),
    ]
