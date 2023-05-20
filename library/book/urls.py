from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [

    path('like/<int:id>', views.like, name='like'),
    path('list_books/<int:id>', views.delete_book, name='delete_book'),
    path('add_book/', views.add_book, name='add_book'),
]