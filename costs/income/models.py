from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    price = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='income')
    timestamp = models.DateField(auto_now_add=True)
    account = models.CharField(max_length=75, default=1)
    balance = models.IntegerField(default=0)
    goal_title = models.CharField(max_length=75, default=None, null=True)
    goal = models.PositiveIntegerField(default=None, null=True)