from rest_framework import generics
from rest_framework.response import Response
from django_filters import rest_framework as filters
from orders.models import Order, OrderItem
from orders.serializers import (
    OrderItemSerializer, OrderSerializer,
    OrderCreateSerializer
)
from orders.utils.send_sms import send_sms


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        send_sms([order.customer.phone], "Your order is placed")
        detail_serializer = OrderSerializer(order)
        return Response(detail_serializer.data)

class ListOrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('customer__id', 'status')


class RetrieveDestroyUpdateOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'id'


class CreateOrderItemView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class RetrieveDestroyUpdateOrderItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_url_kwarg = 'id'
  