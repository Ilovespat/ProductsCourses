from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    '''Модель продукта
    Доступ к продукту устанавливается администратором сайта в админке в модели групп'''
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор курса')
    name = models.CharField(max_length=100, verbose_name='Название курса')
    start = models.DateField(verbose_name='Дата начала курса')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость курса')
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    lessons = models.IntegerField(verbose_name='Количество уроков в курсе')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Lesson(models.Model):
    '''Модель Урока.
    При добавлении уроков меняется количество уроков в модели Продукт'''
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    name = models.CharField(max_length=100, verbose_name='Название урока')
    video_link = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Group(models.Model):
    '''Модель группы.
    Доступ к продукту устанавливается администратором сайта в админке в модели групп'''
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    name = models.CharField(max_length=100, verbose_name='Название')
    students = models.ManyToManyField(User, verbose_name='Ученики курса')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
