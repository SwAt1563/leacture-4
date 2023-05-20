from django.shortcuts import render
from book.models import Book
from author.models import Author

# Create your views here.


def index(request):
    query = request.GET.get('search')  # Get the search query from the GET parameters

    if query:
        # Perform the search query on the Book model
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()  # Retrieve all books if no search query is provided



    context = {'books': books}  # Prepare the context data for rendering the template
    return render(request, 'home/index.html', context)


