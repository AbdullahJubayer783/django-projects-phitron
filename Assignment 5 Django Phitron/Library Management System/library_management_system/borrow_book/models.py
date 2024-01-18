from django.db import models
from users.models import UserAccountModel
from books.models import BookModel
from .constants import TRANSACTION_TYPE
# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(UserAccountModel, related_name = 'transactions', on_delete = models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['timestamp'] 


class BorrowBookModel(models.Model):
    account = models.ForeignKey(UserAccountModel, related_name = 'borrow', on_delete = models.CASCADE)
    book = models.ForeignKey(BookModel,related_name = 'borrowed', on_delete = models.CASCADE)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12, null=True,blank = True)
    created_time = models.DateTimeField(auto_now_add=True)
    is_returnd = models.BooleanField(default = False)

    def __str__(self):
        return self.book.title
    

    

