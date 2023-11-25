from rest_framework.serializers import ModelSerializer
from products.models import Product, ProductFlavour, ProductSize


class ProductSizeSerializer(ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['id','title','active']


class ProductFlavourSerializer(ModelSerializer):
    class Meta:
        model = ProductFlavour
        fields = ['id','title','active']


class ProductSerializer(ModelSerializer):

    class Meta:
        fields = [
            'id','title','description','active', 
            'available_sizes','available_flavours',
            'price'
        ]
        model = Product
        extra_kwargs = {'available_sizes': {'required': False},'available_flavours': {'required': False}}