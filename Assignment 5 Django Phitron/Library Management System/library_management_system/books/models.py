from django.db import models
from categorys.models import CategorysModel
# Create your models here.
class BookModel(models.Model):
    image = models.ImageField(upload_to ='books/media/uploads/',blank=True, null=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    catagory = models.ManyToManyField(CategorysModel)
    borrowprice = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return f'title - {self.title}'

class Comment(models.Model):
    post = models.ForeignKey(BookModel,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Comment By {self.name}"