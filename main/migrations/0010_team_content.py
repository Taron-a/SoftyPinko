# Generated by Django 5.0.2 on 2024-02-19 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_row'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('user_name', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Team_content',
                'verbose_name_plural': 'Team_contents',
            },
        ),
    ]
