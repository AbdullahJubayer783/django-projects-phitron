from django.urls import path
from .views import DepositMoneyView
urlpatterns = [
    path('deposite/',DepositMoneyView.as_view() , name="deposite"),
]