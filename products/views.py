from rest_framework.viewsets import ModelViewSet
from products.models import ProductSize, ProductFlavour, Product
from products.serializers import (
    ProductFlavourSerializer, ProductSizeSerializer,
    ProductSerializer
)


class ProductFlavourViewSet(ModelViewSet):
    queryset = ProductFlavour.objects.all()
    serializer_class = ProductFlavourSerializer

class ProductSizeViewSet(ModelViewSet):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related(
                'available_sizes','available_flavours').all()
    serializer_class = ProductSerializer