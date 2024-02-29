import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .models import Product, Lesson, Group
from .serializers import ProductSerializer, LessonSerializer, GroupSerializer


def login_view(request):
    '''Аутентификация пользователя. После авторизации выполняется запрос с отображением уроков по продуктам,
    доступным пользователю'''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/api/availablelessons/?format=json')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


class ProductsViewSet(viewsets.ModelViewSet):
    '''Представление продуктов'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AvailableProductsViewSet(viewsets.ModelViewSet):
    '''Представление доступных к покупке продуктов, проверка по дате начала курса'''
    queryset = Product.objects.filter(start__gt=datetime.date.today())
    serializer_class = ProductSerializer


class AvailableGroupsViewSet(viewsets.ModelViewSet):
    '''Представление продуктов и групп, доступных пользователю'''
    serializer_class = GroupSerializer

    def get_queryset(self):
        user_groups = Group.objects.filter(students__id=self.request.user.id)
        return user_groups


class AvailableLessonViewSet(viewsets.ModelViewSet):
    '''Представление списка уроков, доступных пользователю'''
    serializer_class = LessonSerializer

    def get_queryset(self):
        user_groups = Group.objects.filter(students__id=self.request.user.id)
        if user_groups:
            product_list = []
            for group in user_groups:
                product = Product.objects.get(id=group.product.id)
                product_list.append(product)
            lessons_list = []
            for product in product_list:
                lesson = Lesson.objects.filter(product=product)
                lessons_list.extend(lesson)
            return lessons_list
        else:
            return []
