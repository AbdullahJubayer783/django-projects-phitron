from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from borrow_book.constants import DEPOSIT , BORROW_BOOK
from datetime import datetime
from django.db.models import Sum
from books.models import BookModel
from borrow_book.models import BorrowBookModel
from borrow_book.forms import (
    DepositForm,
    
)
from borrow_book.models import Transaction

#==================================
def send_transaction_email(user,amount,subject,template):
    message = render_to_string(template,{
        'user' : user,
        'amount' : amount,
    })
    send_email = EmailMultiAlternatives(subject,'',to=[user.email])
    send_email.attach_alternative(message,"text/html")
    send_email.send()

#==================================

class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'deposite.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('home')
    context = None
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # template e context data pass kora
        context.update({
            'title': self.title
        })

        return context


class DepositMoneyView(TransactionCreateMixin):
    template_name = 'deposite.html'
    form_class = DepositForm
    title = 'Deposit'
    success_url = reverse_lazy("home")
    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount 
        account.save(
            update_fields=[
                'balance'
            ]
        )
        send_transaction_email(self.request.user,amount,"Deposite Report","deposite_email.html")
        
        
        return super().form_valid(form)




class BorrowBookView(LoginRequiredMixin,View):
    def get(self,request,id):
        book = BookModel.objects.get(pk=id)
        buyer = self.request.user.account
        alredy_borrowed_book = BorrowBookModel.objects.filter(book=book,account = buyer).first() 
        if alredy_borrowed_book :
            messages.error(self.request,"This book is alredy borrowed")
            
        else:
            
            if buyer.balance >= book.borrowprice:
                buyer.balance-=book.borrowprice
                buyer.save()
                new_transaction = Transaction(
                    account = buyer,
                    amount = book.borrowprice,
                    balance_after_transaction = buyer.balance,
                    transaction_type = BORROW_BOOK
                )
                new_transaction.save()
                BorrowBookModel.objects.create(
                    account = buyer,
                    balance_after_transaction = buyer.balance,
                    book = book
                )
                messages.success(self.request,"Borrowed book")
                send_transaction_email(self.request.user,book.borrowprice,"Borrowing Report","borrow_email.html")
            else:
                messages.error(self.request,"You have no balance")
        return redirect("home")
            



# class TransactionReportView(LoginRequiredMixin, ListView):
#     template_name = 'transactions/transaction_report.html'
#     model = Transaction
#     balance = 0 # filter korar pore ba age amar total balance ke show korbe
    
#     def get_queryset(self):
#         return BorrowBookModel.objects.all()
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({
#             'account': self.request.user.account
#         })

#         return context
# class BorrowBookView(TransactionCreateMixin):
#     def get_initial(self):
#         initial = {'transaction_type': BORROW_BOOK}
#         return initial

#     def form_valid(self, form):
#         amount = form.cleaned_data.get('amount')

#         self.request.user.account.balance -= form.cleaned_data.get('amount')
#         # balance = 300
#         # amount = 5000
#         self.request.user.account.save(update_fields=['balance'])

#         messages.success(
#             self.request,
#             f'Successfully withdrawn {"{:,.2f}".format(float(amount))}$ from your account'
#         )
#         # send_transaction_email(self.request.user,amount,"Deposite Report","transactions/deposite_email.html")
#         return super().form_valid(form)
