from core.models import Book, Order, OrderItem
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ["url", "title", "slug", "author",
                  "image", "price", "short_description"]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ["url", "customer", "address", "phone"]


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["url", "order", "book", "quantity"]
