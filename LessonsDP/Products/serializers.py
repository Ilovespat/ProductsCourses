from rest_framework.serializers import ModelSerializer

from Products.models import Product, Lesson, Group


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'cost', 'start', 'lessons']


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['product', 'name']


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'students', 'product']
