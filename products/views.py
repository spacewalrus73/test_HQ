from rest_framework.viewsets import ReadOnlyModelViewSet
from products.models import Product
from products.models import Lesson
from products.serializers import ProductSerializer
from products.serializers import LessonSerializer
from products.permissions import LessonAccessPermission


class ProductListViewSet(ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonListViewSet(ReadOnlyModelViewSet):

    # queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (LessonAccessPermission, )

    def get_queryset(self):
        res = Lesson.objects.filter(product__id=self.kwargs["pk"])
        print(res)
        return res
