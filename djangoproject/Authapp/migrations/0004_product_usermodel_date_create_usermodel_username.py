# Generated by Django 5.0.6 on 2024-05-31 12:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authapp', '0003_remove_usermodel_date_create_usermodel_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField()),
                ('stocks', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='usermodel',
            name='date_create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
