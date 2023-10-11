from django.shortcuts import get_object_or_404, render
from .models import Book #importing Book class from model
from django.http import Http404
from django.db.models import Avg
# Create your views here.
def index(request):
    books=Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating=books.aggregate(Avg("rating")) #rating_avg
    return render(request, "book_outlet/index.html",{
        "books":books,
        "total_number_of_books":num_books,
        "average_rating": avg_rating
    })

def book_detail(request, id):
    # try:
    #      book = Book.objects.get(pk=id)#pk is That's a special named argument,which you can always use to query the field,which is set up as a primary key.
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, pk=id)
    return render(request, "book_outlet/book_detail.html",{
        
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestseller":book.is_bestselling

    })