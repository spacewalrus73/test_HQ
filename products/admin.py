from django.contrib import admin
from products.models import Product, Lesson, StudentsGroup, Access
# Register your models here.

admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(StudentsGroup)
admin.site.register(Access)
