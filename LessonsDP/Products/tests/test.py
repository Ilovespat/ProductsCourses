from django.test import TestCase
from Products.models import Product
from django.urls import reverse
import datetime
from Products.serializers import ProductSerializer


class ProductApiTestCase(TestCase):

    def test_get(self):
        Course1 = Product.objects.create(creator='', name='TestCourse', start=datetime.date.today(), cost=1000,
                                         min_users=0, max_users=1, lessons=0)
        Course2 = Product.objects.create(creator='', name='TestCourse2', start=datetime.date.today(), cost=2000,
                                         min_users=0, max_users=1, lessons=0)
        url = reverse('courses-list')
        response = self.client.get(url)
        serializer_data = ProductSerializer([Course1, Course2], many=True).data
        self.assertEqual(serializer_data, response.data)



