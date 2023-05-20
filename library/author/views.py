from django.shortcuts import render, get_object_or_404
from .models import Author
from book.models import Book

# Create your views here.




def profile_view(request, slug):
    # get the author profile

    author = get_object_or_404(Author, slug=slug)
    books = Book.objects.filter(author=author)

    context = {'author': author, 'books': books}
    return render(request, 'author/user_profile.html', context)


