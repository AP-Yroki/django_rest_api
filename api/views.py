from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView
from .models import Book
from .serializers import BookSerializer


# Create your views here.

class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
def bookslist(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def bookCurrent(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['POST'])
def bookCreate(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def bookPut(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(data=request.data, instance=book, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PATCH'])
def bookPatch(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(data=request.data, instance=book, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
