from django.shortcuts import render
from . import models
from . import forms
from django.views.generic import CreateView , UpdateView ,DeleteView , DetailView
# Create your views here.
class DetailsBookView(DetailView):
    model = models.BookModel
    template_name = 'detail_book.html'
    pk_url_kwarg = 'id'
    context_object_name = 'book'

    def post(self,request,*args ,**kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request,*args ,**kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
