from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserAccountModel(models.Model):
    user = models.OneToOneField(User,related_name="account",on_delete=models.CASCADE )
    balance = models.DecimalField(default=0,max_digits=8,decimal_places=2)
    def get_balance(self):
        return self.balance
    def __str__(self) :
        return self.user.username
