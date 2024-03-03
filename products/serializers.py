from rest_framework import serializers
from products.models import Product, Lesson


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["creator", "name", "start_date", "cost"]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class ProductStatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
