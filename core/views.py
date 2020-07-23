from django.shortcuts import render
from rest_framework import viewsets
from core.models import Book, Order, OrderItem
from core import serizlizers


class BookViews(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serizlizers.BookSerializer


class OrderViews(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serizlizers.OrderSerializer


class OrderIemViews(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = serizlizers.OrderItemSerializer
