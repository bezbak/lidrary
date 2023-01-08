from django.shortcuts import render, redirect
from apps.posts.models import Books, Category

# Create your views here.

def index(request):
    books = Books.objects.all() 
    context = {
        'books': books,
    }
    return render(request, 'index.html', context)

def main(request,id):
    book = Books.objects.get(id = id)
    categories = Category.objects.all()
    books = Books.objects.all()
    context = {
        'book': book,
        'books': books,
        'cotegories':categories,
    }
    return render(request, 'books-detail.html', context)
    