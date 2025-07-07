from django.shortcuts import render
from .models import BorrowedBook

def home(request):
    return render(request, 'second_app/home.html')

def borrowed_books(request):
    borrowed_books_data = BorrowedBook.objects.all()

    context = {
        'borrowed_books_data': borrowed_books_data
    }

    return render(request, 'second_app/borrowed_books.html', context)