from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Book, Like
# Create your views here.
from .forms import BookForm
from author.models import Author

def like(request, id):
    # let the user make a like  to a book
    book = Book.objects.get(id=id)
    user = request.user

    if not Like.objects.filter(book=book, user=user).exists():
        Like.objects.create(book=book, user=user)

    return HttpResponseRedirect(reverse('home:index'))


def delete_book(request, id):
    # delete a book
    book = Book.objects.get(id=id)
    user = request.user

    if book.author.user == user:
        book.delete()

    return HttpResponseRedirect(reverse('home:index'))


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():

            Book.objects.create(author=request.user.author,title=form.cleaned_data['title'],
                                description=form.cleaned_data['description'])

            return HttpResponseRedirect(reverse('home:index'))  # Replace 'book_list' with your book list URL name
    else:
        form = BookForm()
    return render(request, 'book/add_book.html', {'form': form})


