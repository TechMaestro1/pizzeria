from rest_framework import routers

from products.views import (
    ProductViewSet, ProductFlavourViewSet,
    ProductSizeViewSet
)

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'flavours', ProductFlavourViewSet)
router.register(r'sizes', ProductSizeViewSet,basename='sizes')

urlpatterns = router.urls