from django.db import models
from django.contrib.auth.models import User

class Spending(models.Model):
    price = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spendings')
    category = models.CharField(max_length=75, default=None)
    timestamp = models.DateField(auto_now_add=True)
    account = models.CharField(max_length=75, default=1)
    balance = models.PositiveIntegerField(default=0)
