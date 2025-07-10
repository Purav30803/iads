from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponse
from .forms import FeedbackForm,SearchForm,OrderForm

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

def getFeedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data['feedback']
            if feedback == 'B':
                choice = ' to borrow books.'
            elif feedback == 'P':
                choice = ' to purchase books.'
            else: choice = ' None.'
            return render(request, 'myapp/fb_results.html', {'choice':choice})
        else:
            return HttpResponse('Invalid data')
    else:
        form = FeedbackForm()
        return render(request, 'myapp/feedback.html', {'form':form})

def findbooks(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data.get('category')  # might be None
            max_price = form.cleaned_data['max_price']

            if category:
                booklist = Book.objects.filter(category=category, price__lte=max_price)
            else:
                booklist = Book.objects.filter(price__lte=max_price)

            return render(request, 'myapp/results.html', {
                'name': name,
                'category': category,
                'booklist': booklist,
            })
        else:
            return HttpResponse("Invalid data")
    else:
        form = SearchForm()
        return render(request, 'myapp/findbooks.html', {'form': form})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            books = form.cleaned_data['books']
            order = form.save(commit=False)
            member = order.member
            type = order.order_type
            order.save()  # Save the order object first

            # Important: save M2M relationship after saving the instance
            order.books.set(books)  # ✅ Ensures books are associated with order
            order.save()

            if type == 1:  # 1 = Borrow
                for b in books:
                    member.borrowed_books.add(b)

            return render(request, 'myapp/order_response.html', {
                'books': books,
                'order': order
            })
        else:
            return render(request, 'myapp/placeorder.html', {'form': form})
    else:
        form = OrderForm()
        return render(request, 'myapp/placeorder.html', {'form': form})