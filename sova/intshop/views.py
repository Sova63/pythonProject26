from django.shortcuts import render, redirect, get_object_or_404
from .models import Product_movie,Product_book,Product_music
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def movie(request):
    movies = Product_movie.objects.all()
    items_per_page = request.GET.get('items_per_page',3)
    paginator = Paginator(movies,items_per_page)
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)
    return render(request, 'movie.html', {'movies': movies,'paginator': paginator})

def viewing_movie(request, pk):
    movie = get_object_or_404(Product_movie, pk=pk)
    return render(request, 'viewing_movie.html', {'movie': movie})

def book(request):
    books = Product_book.objects.all()
    items_per_page = request.GET.get('items_per_page',3)
    paginator = Paginator(books,items_per_page)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(request, 'book.html', {'books': books,'paginator': paginator})

def viewing_book(request, pk):
    book = get_object_or_404(Product_book, pk=pk)
    return render(request, 'viewing_book.html', {'book': book})

def music(request):
    musics = Product_music.objects.all()
    items_per_page = request.GET.get('items_per_page',3)
    paginator = Paginator(musics,items_per_page)
    page_number = request.GET.get('page')
    musics = paginator.get_page(page_number)
    return render(request, 'music.html', {'musics': musics,'paginator': paginator})

def viewing_music(request, pk):
    music = get_object_or_404(Product_music, pk=pk)
    return render(request, 'viewing_music.html', {'music': music})




def search_results(request):
    query = request.GET.get('query')
    if query:
        movies = Product_movie.objects.filter(Q(name__icontains=query) | Q(director__icontains=query))
        books = Product_book.objects.filter(Q(name__icontains=query) | Q(author__icontains=query))
        musics = Product_music.objects.filter(Q(name__icontains=query) | Q(author__icontains=query) | Q(executor__icontains=query))
        return render(request, 'search_results.html', {'movies': movies, 'books': books, 'musics': musics, 'query': query})
    else:
        return render(request, 'search_results.html', {'query': query})