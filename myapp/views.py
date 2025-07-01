from django.shortcuts import render, get_object_or_404
from .models import Book
# Create your views here.


def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def index_view(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def index(request):
    booklist = Book.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'booklist': booklist})


def about(request):
    return render(request, 'myapp/about.html')

def detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'myapp/detail.html', {'book': book})