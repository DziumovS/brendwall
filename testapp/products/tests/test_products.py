import pytest
from decimal import Decimal
from rest_framework import status
from rest_framework.test import APIClient
from products.models import Product

@pytest.mark.django_db
class TestProductAPI:
    def setup_method(self):
        self.client = APIClient()

    def test_create_product(self):
        product_data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': 10.99
        }
        response = self.client.post('/api/products/', product_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        product = Product.objects.get(name='Test Product')
        assert product.description == 'This is a test product.'
        assert product.price == Decimal('10.99')

    def test_get_products(self):
        Product.objects.create(name='Test Product', description='This is a test product.', price=10.99)
        response = self.client.get('/api/products/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['name'] == 'Test Product'
        assert response.data[0]['description'] == 'This is a test product.'
        assert response.data[0]['price'] == '10.99'

    def test_create_product_invalid(self):
        product_data = {
            'name': 'Invalid Product',
            'description': 'This product has an invalid price.',
            'price': -5.99
        }
        response = self.client.post('/api/products/', product_data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'non_field_errors' in response.data
