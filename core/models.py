from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, null=False, blank=False)
    author = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(default=0)
    short_description = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.title)


class Order(models.Model):
    customer = models.CharField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    phone = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.id) + " " + str(self.customer) + " " + str(self.phone)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "Order: %s, book: %s, quantity: %s" % (str(self.order), str(self.book), str(self.quantity))
