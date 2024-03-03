from django.db.models import F, Count, Avg

from products.models import Lesson
from products.models import Product
from products.models import StudentsGroup
from products.models import Access
from clients.models import Client


def count_lessons(id):
    count = Lesson.objects.filter(product__id=id).count()

    Product.objects.filter(id=id).update(
        lessons_count=count
    )


def delete_lesson_from_count(id):
    Product.objects.filter(id=id).update(
        lessons_count=F("lessons_count") - 1
    )


def collect_statistic(product):

    groups = StudentsGroup.objects.filter(
        product__id=product.id).prefetch_related("students")

    students_count = groups.aggregate(total=Count('students'))["total"]

    students_avg = groups.aggregate(fill=Avg('students'))

    fill_rate = (students_avg["fill"] / product.max_students) * 100

    total_users = Client.objects.all().count()

    count_accesses = Access.objects.filter(
        product_id=product.id
    ).count()

    purchase_rate = (count_accesses / total_users) * 100

    Product.objects.filter(id=product.id).update(
        students_count=students_count,
        fill_rate=fill_rate,
        purchase_rate=purchase_rate
    )
