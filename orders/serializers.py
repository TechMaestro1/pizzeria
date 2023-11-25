from rest_framework import  serializers
from orders.models import OrderItem, Order
from accounts.serializers import CustomerSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'id','order','quantity','product_size',
            'product_flavour','product','price'
        ]
        read_only_fields = ['id','price','order']


class  OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    order_items = OrderItemSerializer(source='orderitem_set',many=True)

    class Meta:
        model = Order
        fields = ['id','customer','status','total_price','order_items']
        read_only_fields = ['total_price']

    def validate_status(self, value):
        if value == 'delivered':
            raise serializers.ValidationError("Changing to this status is prohibited")
        return value


class OrderCreateSerializer(serializers.ModelSerializer):
    order_items = serializers.ListField(
                child=OrderItemSerializer(),
                allow_empty=True
    )
    class Meta:
        model = Order 
        fields = ['id','customer','status','total_price','order_items']
        read_only_fields = ['total_price','status']
    
    def create(self, validated_data):
        order_items = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for item in order_items:
            OrderItem.objects.create(
                order=order,**item
            )
        order.save()
        return order