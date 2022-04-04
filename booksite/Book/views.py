from django.shortcuts import render
from .models import BookData
from django.core.paginator import Paginator


# Create your views here.
def book_list(request):
    book_object = BookData.objects.all()
    books_per_page = 5
    book_name = request.GET.get('book_name')

    if book_name != '' and book_name is not None:
        book_object = book_object.filter(name__icontains=book_name)

    paginator = Paginator(book_object, books_per_page)
    page = request.GET.get('page')

    book_object = paginator.get_page(page)

    return render(request, 'Book/book_list.html', {'book_object': book_object})
