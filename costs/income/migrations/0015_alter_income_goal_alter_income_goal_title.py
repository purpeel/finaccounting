# Generated by Django 4.2.8 on 2024-12-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0014_alter_income_balance_alter_income_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='goal',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='goal_title',
            field=models.CharField(default='', max_length=75, null=True),
        ),
    ]
