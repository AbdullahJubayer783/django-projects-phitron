from books.models import BookModel
from categorys.models import CategorysModel
from borrow_book.models import BorrowBookModel
from django.views.generic import ListView

class HomePageView(ListView):
    template_name = 'index.html'
    model = BookModel

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = CategorysModel.objects.get(slug = category_slug)
            return BookModel.objects.filter(catagory=category)
        return BookModel.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategorysModel.objects.all()
        context['objects'] = BorrowBookModel.objects.all()
        return context 