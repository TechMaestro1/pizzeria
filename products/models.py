import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProductSize(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title =  models.CharField(_('Product Title'),max_length=255,null=False,blank=False)
    active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    updated_date = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = _('Product Size')
        verbose_name_plural = _('Products Sizes')


class ProductFlavour(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title =  models.CharField(_('Product Flavour'), max_length=255,null=False,blank=False)
    active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    updated_date = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = _('Product Flavour')
        verbose_name_plural = _('Products Flavours')
    

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title =  models.CharField(_('Product Flavour'), max_length=255,null=False,blank=False)
    description = models.TextField(_('Product Description'), null=True, blank=True)
    active = models.BooleanField(default=True)
    available_sizes = models.ManyToManyField(ProductSize, verbose_name=_('Available Sizes'))
    available_flavours = models.ManyToManyField(ProductFlavour, verbose_name=_('Available Flavours'))
    price = models.DecimalField(_('Product Proce'), max_digits=15, decimal_places=2)
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    updated_date = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
