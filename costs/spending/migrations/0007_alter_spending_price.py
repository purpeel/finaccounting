# Generated by Django 4.2.8 on 2023-12-18 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0006_alter_spending_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spending',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
