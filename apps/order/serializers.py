from rest_framework import serializers

from order.models import Material, Order


class MaterialSerializer(serializers.ModelSerializer):
    """ 物料信息 """
    class Meta:
        model = Material
        fields = ('id', 'order', 'material', 'number')


class OrderSerializer(serializers.ModelSerializer):
    """ 订单信息 """
    status = serializers.CharField(source='get_status_display', required=False)
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d')
    material = MaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'material', 'remark', 'sales', 'order_date', 'delivery_time', 'status', 'produce', 'created_at')
