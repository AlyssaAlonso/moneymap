# Generated by Django 4.2.7 on 2023-11-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_expense_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
