from rest_framework import routers
from core import views
from django.urls import path, include

route = routers.DefaultRouter()
route.register(r'book', views.BookViews)
route.register(r'order', views.OrderViews)
route.register(r'order-item', views.OrderIemViews)

urlpatterns = [
    path('', include(route.urls))
]
