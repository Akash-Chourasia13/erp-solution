from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = []

router.register(r'productlist', views.productlistViewSet, basename="productlist")

urlpatterns += router.urls
