# Generated by Django 4.2.7 on 2023-11-29 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_bill_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.CharField(choices=[('Essential', 'Essential'), ('Nonessential', 'Nonessential')], default='Essential', max_length=255),
        ),
    ]