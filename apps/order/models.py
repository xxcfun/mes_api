from django.contrib.auth import get_user_model
from django.db import models
from order.choices import Status
from utils.models import CommonModel

User = get_user_model()


class Order(CommonModel):
    """ 从SQL server里面抓取的订单信息，保存这里 """
    id = models.IntegerField('订单编号', unique=True, primary_key=True)
    customer = models.CharField('客户名称', max_length=128)
    remark = models.CharField('附加说明', max_length=512, blank=True, null=True)
    sales = models.CharField('经手业务', max_length=16)
    order_date = models.CharField('订单建立时间', max_length=16, blank=True, null=True)
    delivery_time = models.CharField('预计发货时间', max_length=64, blank=True, null=True)
    status = models.SmallIntegerField('生产进度', choices=Status.choices, default=Status.STATUS_BL)
    # 这个produce字段目前先不使用，后面先引入product表来用
    produce = models.ForeignKey(User, verbose_name='生产人员', related_name='order', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '所有订单'
        verbose_name_plural = verbose_name
        db_table = 'master_order'
        ordering = ['-id']

    def __str__(self):
        return self.id


class Material(models.Model):
    """ 物料信息 """
    id = models.IntegerField('物料编号', unique=True, primary_key=True)
    order = models.ForeignKey(Order, verbose_name='订单编号', related_name='material', on_delete=models.CASCADE)
    material = models.CharField('物料名称', max_length=256)
    number = models.IntegerField('数量')

    class Meta:
        verbose_name = '物料信息'
        verbose_name_plural = verbose_name
        db_table = 'material'
        ordering = ['-id']

    def __str__(self):
        return self.id
