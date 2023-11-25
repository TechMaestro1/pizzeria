from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import ProductSize, ProductFlavour, Product

class ProdcutTests(APITestCase):

    def test_create_product_size(self):

        url = reverse('sizes-list')
        data = {'title': 'Medium'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductSize.objects.count(), 1)
        self.assertEqual(ProductSize.objects.get().title, 'Medium')
        self.assertIsNotNone(ProductSize.objects.get().id)