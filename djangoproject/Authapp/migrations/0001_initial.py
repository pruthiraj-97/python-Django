# Generated by Django 5.0.6 on 2024-05-30 06:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Image/')),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('AM', 'ADMIN'), ('US', 'USER'), ('OW', 'OWNER')], max_length=2)),
            ],
        ),
    ]
