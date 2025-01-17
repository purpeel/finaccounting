# Generated by Django 4.2.8 on 2024-12-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0015_alter_income_goal_alter_income_goal_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='goal',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='goal_title',
            field=models.CharField(default=None, max_length=75, null=True),
        ),
    ]
