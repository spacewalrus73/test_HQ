from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete

from products.models import Access
from products.models import Lesson
from products.distributor import assign_group
from products.support_funcs import count_lessons
from products.support_funcs import collect_statistic
from products.support_funcs import delete_lesson_from_count


@receiver(signal=post_save, sender=Access)
def post_save_create_students_groups(sender, instance, created, **kwargs):

    if created:
        assign_group(instance.product, instance.student)


@receiver(signal=post_save, sender=Lesson)
def post_save_count_lessons(sender, instance, created, **kwargs):

    if created:
        count_lessons(instance.product.id)


@receiver(signal=pre_delete, sender=Lesson)
def pre_delete_count_lessons(sender, instance, **kwargs):

    delete_lesson_from_count(instance.product.id)


@receiver(signal=post_save, sender=Access)
def post_save_collect_statistic(sender, instance, created, **kwargs):

    collect_statistic(instance.product)
