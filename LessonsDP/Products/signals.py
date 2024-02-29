from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, Lesson


@receiver(post_save, sender=Lesson)
def update_lessons_count(sender, instance, **kwargs):
    '''Сигнал - при добавлении новых уроков, обновляет модель продукта'''
    product = instance.product
    product.lessons = Lesson.objects.filter(product=product).count()
    product.save()
