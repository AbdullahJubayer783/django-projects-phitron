from django.shortcuts import render , redirect
from django.views.generic import FormView 
from django.contrib.auth.views import LoginView
from .forms import UserCreationForm , UserDataChangeForm , UserAccountForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import login , logout
from django.contrib.auth.views import LogoutView 
from django.views.generic import CreateView , UpdateView , DeleteView
from .models import UserAccountModel 
# Create your views here.
class UserCreationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserAccountForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        balance = UserAccountModel.objects.create(user=user,balance=0)
        balance.save()
        login(self.request,user)
        return super().form_valid(form)

class ProfileUpdateView5(View):
    template_name = 'profile.html'
    def get(self,request):
        form = UserDataChangeForm(instance=request.user)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = UserDataChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request,self.template_name,{'form':form})
from borrow_book.models import BorrowBookModel
class ProfileUpdateView(UpdateView):
    model = UserAccountModel
    form_class = UserDataChangeForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile') 

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = BorrowBookModel.objects.all()
        return context 
    
class RetrunedBookView(DeleteView):
    model = BorrowBookModel
    template_name = 'return.html'
    success_url = reverse_lazy("home")
    pk_url_kwarg = 'id'

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self) :
        return reverse_lazy("home")
    
class UserLogoutview(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy("profile")
    