from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from order import views

router = DefaultRouter()

router.register(r'order', views.OrderViewset, basename='order')
router.register(r'order/bl', views.OrderViewsetBL, basename='order_bl')

urlpatterns = [
    re_path('^', include(router.urls))
]
