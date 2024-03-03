from django.db import models
from django.utils import timezone
from clients.models import Client


class Product(models.Model):

    creator = models.ForeignKey(Client, on_delete=models.PROTECT)
    name = models.CharField(max_length=155, unique=True)
    start_date = models.DateTimeField(default=None)
    cost = models.DecimalField(default=0.0, decimal_places=3, max_digits=10)
    max_students = models.PositiveIntegerField()
    min_students = models.PositiveIntegerField()
    lessons_count = models.PositiveIntegerField(null=True)
    students_count = models.PositiveIntegerField(null=True, blank=True)
    fill_rate = models.PositiveIntegerField(null=True, blank=True)
    purchase_rate = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}-{self.cost}-{self.creator}"

    def is_started(self):
        return self.start_date < timezone.now()


class Lesson(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField()


class StudentsGroup(models.Model):

    students = models.ManyToManyField(Client, blank=True)
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Access(models.Model):

    student = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["student", "product"]
