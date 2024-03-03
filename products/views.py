from django.utils import timezone
from rest_framework.viewsets import ReadOnlyModelViewSet
from products.models import Product
from products.models import Lesson
from products.serializers import ProductSerializer
from products.serializers import LessonSerializer
from products.permissions import LessonAccessPermission
from products.serializers import ProductStatisticSerializer


class ProductListViewSet(ReadOnlyModelViewSet):

    queryset = Product.objects.filter(start_date__gt=timezone.now())
    serializer_class = ProductSerializer


class LessonListViewSet(ReadOnlyModelViewSet):

    serializer_class = LessonSerializer
    permission_classes = (LessonAccessPermission, )

    def get_queryset(self):
        return Lesson.objects.filter(
            product__id=self.kwargs["pk"]
        ).select_related("product")


class ProductStatisticViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductStatisticSerializer
    queryset = Product.objects.all().select_related("creator")
