from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from .views import BookView, bookslist, bookCurrent, bookCreate, bookPut, \
    bookPatch


urlpatterns = [
    path('', BookView.as_view({'get':'list', 'post': 'create'})),
    path('bookslist/', bookslist),
    path('bookCurrent/<int:pk>/', bookCurrent),
    path('bookAdd/', bookCreate),
    path('bookPut/<int:pk>/', bookPut),
    path('bookPatch/<int:pk>/', bookPatch),
]