from math import ceil
from products.models import StudentsGroup
from products.models import Access
from django.db.models import Count, Min


def chunks(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


def distribute(product):

    groups = StudentsGroup.objects.filter(
        product__id=product.id).select_related("students")

    total_students = groups.aggregate(total=Count("students"))["total"] + 1

    new_groups_count = ceil(total_students / product.min_students)

    if not new_groups_count:
        new_groups_count = 1

    students = [
        obj.student for obj in Access.objects.filter(
            product__id=product.id).prefetch_related("student")
    ]

    chunked_students = list(chunks(students, product.min_students))

    groups.delete()

    for group_num, students_cut in zip(range(new_groups_count), chunked_students):
        StudentsGroup.objects.create(
            product=product,
            name=f"{group_num}-{product.name}"
        ).students.add(*students_cut)


def find_minimum_students_groups(product):
    groups = StudentsGroup.objects.filter(
        product__id=product.id).prefetch_related("students")

    student_count = groups.annotate(student_count=Count('students'))

    min_students_count = student_count.aggregate(Min("student_count"))

    return student_count.filter(
        student_count=min_students_count["student_count__min"]
    )


def assign_group(product, student):
    groups_min_students = find_minimum_students_groups(product)

    distributed = False

    if groups_min_students and not product.is_started():

        current_group = groups_min_students[0]
        students_count = current_group.students.count()

        if ((product.max_students > students_count >= product.min_students)
                or (students_count < product.min_students)):

            current_group.students.add(student)
            distributed = True

    if not distributed:
        distribute(product)
