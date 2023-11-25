from django.urls import include, path
from orders.views import (
    ListOrderView,RetrieveDestroyUpdateOrderView,
    CreateOrderView, CreateOrderItemView,
    RetrieveDestroyUpdateOrderItemView
)

urlpatterns = [
    path('orders/',ListOrderView.as_view(),name='orders-create-list'),
    path('create-order/',CreateOrderView.as_view(),name='create-order'),
    path('orders/<uuid:id>/',RetrieveDestroyUpdateOrderView.as_view(),
            name="orders-get-delete-update"),
    path('order-items/',CreateOrderItemView.as_view(),
            name='order-items-create'),
    path('order-items/<uuid:id>/',RetrieveDestroyUpdateOrderItemView.as_view(),
            name='order-items-get-destroy-update')
]