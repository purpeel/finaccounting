# Generated by Django 4.2.8 on 2024-12-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0010_alter_income_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
