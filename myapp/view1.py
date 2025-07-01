# views.py
from django.shortcuts import render
from .models import Book, Publisher

def index(request):
    books = Book.objects.all().order_by('id')
    publishers = Publisher.objects.all().order_by('-city')
    return render(request, 'index.html', {
        'books': books,
        'publishers': publishers,
    })

def about(request):

    return render(request, 'myapp_about.html')