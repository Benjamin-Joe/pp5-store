"Test File For Products App"
from django.test import TestCase
from .models import Category, Product


class TestModels(TestCase):

    def test_category_return_string(self):
        "Test for returning category name"
        cat = Category(name='Test')
        self.assertEqual(str(cat), 'Test')

    def test_product_string_method_returns_title(self):
        "Test for returning product title"
        product = Product(title='Test Todo Item')
        self.assertEqual(str(product), 'Test Todo Item')
