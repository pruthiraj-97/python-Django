# Generated by Django 5.0.6 on 2024-05-31 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
