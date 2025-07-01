from django.shortcuts import render, get_object_or_404
from .models import Book

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'myapp_detail.html', {
        'book': book
    })