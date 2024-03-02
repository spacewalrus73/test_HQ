from django.db.models import F
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from products.models import Access
from products.models import StudentsGroup
from products.models import Lesson
from products.models import Product


@receiver(signal=post_save, sender=Access)
def post_save_create_students_groups(sender, instance, created, **kwargs):

    if created:
        groups = StudentsGroup.objects.filter(product=instance.product)

        distributed = False

        if instance.product.is_started():
            for group in groups:
                if instance.product.max_students > group.students.count():
                    group.students.add(instance.student)
                    distributed = True
                    break

            if not distributed:
                StudentsGroup.objects.create(
                    product=instance.product
                ).students.add(instance.student)
        else:
            return


@receiver(signal=post_save, sender=Lesson)
def post_save_count_lessons(sender, instance, created, **kwargs):

    if created:

        count = Lesson.objects.filter(product=instance.product).count()
        Product.objects.filter(id=instance.product.id).update(
            lessons_count=count
        )


@receiver(signal=pre_delete, sender=Lesson)
def pre_delete_count_lessons(sender, instance, **kwargs):

    Product.objects.filter(
        id=instance.product.id
    ).update(lessons_count=F("lessons_count") - 1)
