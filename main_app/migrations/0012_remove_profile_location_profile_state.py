# Generated by Django 4.2.7 on 2023-11-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_income_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='YourDefaultState', max_length=255),
        ),
    ]
