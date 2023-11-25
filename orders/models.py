import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from accounts.models import Customer
from products.models import Product, ProductFlavour, ProductSize


class Order(models.Model):
    ORDER_STATUS = (
        ('draft',_('Draft')),
        ('processing',_('Processing')),
        ('cancelled', _('Cancelled')),
        ('delivered', _('Delivered'))
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    status = models.CharField(_('Order Status'), max_length=20, choices=ORDER_STATUS,default='draft')
    total_price = models.DecimalField(_('Order Cost'), decimal_places=2, max_digits=15)
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    updated_date = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.id)
    
    def __len__(self):
        return sum(x.quantity for x in self.orderitem_set.all())

    @property
    def order_items(self):
        return self.orderitem_set.all()
    
    def save(self, *args, **kwargs):
        self.total_price = sum(x.price for x in self.orderitem_set.all()  )
        super(Order,self).save(*args, **kwargs)


    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    quantity = models.PositiveSmallIntegerField(default=1)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_size = models.ForeignKey(ProductSize, on_delete=models.SET_NULL, null=True)
    product_flavour = models.ForeignKey(ProductFlavour, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(_('Order Item Price'), max_digits=15, decimal_places=2)

    def save(self, *args, **kwargs):
        self.price = self.quantity * self.product.price
        super(OrderItem,self).save(*args, **kwargs)


    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')
