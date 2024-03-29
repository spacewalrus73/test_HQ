"""
URL configuration for test_HQ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products.views import ProductListViewSet
from products.views import LessonListViewSet
from products.views import ProductStatisticViewSet
from clients.views import ClientLoginView
from clients.views import ClientLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('login/', ClientLoginView.as_view(), name="login"),
    path('logout/', ClientLogoutView.as_view(), name="logout"),
    path('products/', ProductListViewSet.as_view({'get': 'list'}), name="list_product"),  # noqa: E501
    path('products/<int:pk>/lessons/', LessonListViewSet.as_view({'get': 'list'})),  # noqa: E501
    path('products/statistics/', ProductStatisticViewSet.as_view({'get': 'list'}))  # noqa: E501
]
