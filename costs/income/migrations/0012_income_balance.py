# Generated by Django 4.2.8 on 2024-12-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0011_alter_income_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
