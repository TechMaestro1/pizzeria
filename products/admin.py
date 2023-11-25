from django.contrib import admin
from .models import (ProductSize,ProductFlavour, Product)


# Register your models here.
admin.site.register(ProductSize)
admin.site.register(ProductFlavour)
admin.site.register(Product)