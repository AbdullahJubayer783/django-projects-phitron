from django.urls import path
from borrow_book.views import BorrowBookView
from . import views
urlpatterns = [
    path('detail/<int:id>/', views.DetailsBookView.as_view() , name = 'detail_book'),
    path('book/<int:id>', BorrowBookView.as_view() , name = 'borrow_book'),
]