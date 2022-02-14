from django.db.models import Q
from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from order import serializers
from order.models import Order, Material
from utils.permissions import IsOwnerOrReadOnly
from order.choices import Status


class Pagination(PageNumberPagination):
    """ 分页基础类 """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class OrderViewset(viewsets.ModelViewSet):
    """ 订单管理 GET 查询 """
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = Pagination
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        query = Q(is_valid=True, status=Status.STATUS_BL)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__icontains=customer)
        start_time = self.request.GET.get('start_time', None)
        end_time = self.request.GET.get('end_time', None)
        if start_time and end_time:
            query = query & Q(created_at__range=(start_time, end_time))
        queryset = Order.objects.filter(query)
        return queryset


class OrderViewsetBL(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """ 订单 POST 备料 """
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = Status.STATUS_PD
        instance.save()
        serializer = self.get_serializer(instance).data
        return Response(serializer)


class MaterialViewset(viewsets.ModelViewSet):
    """ 物料管理 """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = serializers.MaterialSerializer

    def get_queryset(self):
        queryset = Material.objects.all()
        return queryset


class OrderViewsetSC(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """ 订单 POST 生产相关操作 """
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # 非订单完成状态，那么订单状态+1
        if instance.status != Status.STATUS_DDWC:
            instance.status += 1
        instance.save()
        serializer = self.get_serializer(instance).data
        return Response(serializer)
