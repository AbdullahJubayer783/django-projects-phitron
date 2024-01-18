from django.urls import path
from .views import UserCreationView , UserLoginView , UserLogoutview , ProfileUpdateView , RetrunedBookView
urlpatterns = [
    path('signup/',UserCreationView.as_view() , name="registar"),
    path('login/',UserLoginView.as_view() , name="login"),
    path('logout/',UserLogoutview.as_view() , name="logout"),
    path('profile/',ProfileUpdateView.as_view() , name="profile"),
    path('return/<int:id>',RetrunedBookView.as_view() , name="return"),
]