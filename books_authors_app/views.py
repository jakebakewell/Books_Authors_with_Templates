from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        "all_books": Book.objects.all(),
    }
    return render(request, 'index.html', context)

def process_book(request):
    title = request.POST['title']
    description = request.POST['description']
    Book.objects.create(title = title, desc = description)
    return redirect('/')

def process_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    Author.objects.create(first_name = first_name, last_name = last_name, notes = notes)
    return redirect('/authors')

def books(request, id_num):
    context = {
        "book": Book.objects.get(id=id_num),
        "non_authors": Author.objects.exclude(books__id=id_num)
    }
    return render(request, 'books.html', context)

def add_author(request):
    author_id = request.POST['author_to_add']
    book_id = request.POST['book_to_add_author_to']
    author_to_add = Author.objects.get(id=author_id)
    book_added_to = Book.objects.get(id=book_id)
    book_added_to.authors.add(author_to_add)
    return redirect('/')

def authors(request):
    context = {
        "all_authors": Author.objects.all(),
    }
    return render(request, 'authors.html', context)

def authors_specific(request, id_num):
    context = {
        "author": Author.objects.get(id=id_num),
        "non_books": Book.objects.exclude(authors__id=id_num)
    }
    return render(request, 'authors_specific.html', context)

def add_book(request):
    author_id = request.POST['author_added_to']
    book_id = request.POST['book_to_add']
    author_added_to = Author.objects.get(id=author_id)
    book_to_add= Book.objects.get(id=book_id)
    author_added_to.books.add(book_to_add)
    return redirect('/authors')
