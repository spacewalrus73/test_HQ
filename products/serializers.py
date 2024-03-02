from rest_framework import serializers
from products.models import Product, Lesson


class ProductSerializer(serializers.ModelSerializer):

    lessons_count = serializers.IntegerField()

    class Meta:
        model = Product
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
