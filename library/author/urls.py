from django.urls import path
from . import views

app_name = 'author'
urlpatterns = [

    path('profile_view/<slug:slug>', views.profile_view, name='profile_view'),

]