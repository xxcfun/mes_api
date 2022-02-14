from django.contrib.auth import get_user_model
from django.db import models

from order.choices import Status
from order.models import Order
from utils.models import CommonModel

User = get_user_model()


class ProductOrder(CommonModel):
    """ 生产表 """
    order = models.ForeignKey(Order, verbose_name='料单信息', on_delete=models.CASCADE)
    number = models.CharField('生产数量', default=0)
    produce = models.ForeignKey(User, verbose_name='生产人员', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '生产信息'
        verbose_name_plural = verbose_name
        db_table = 'product_order'
        ordering = ['-id']

    def __str__(self):
        return self.id


# 这部分先不要了，直接用外键的方式将订单信息拉过来
# class ProductMaterial(models.Model):
#     """ 物料信息 """
#     product_order = models.ForeignKey(ProductOrder, verbose_name='订单编号', related_name='product_material', on_delete=models.CASCADE)
#     material = models.CharField('物料名称', max_length=256)
#     number = models.IntegerField('数量')
#
#     class Meta:
#         verbose_name = '物料信息'
#         verbose_name_plural = verbose_name
#         db_table = 'product_material'
#         ordering = ['-id']
#
#     def __str__(self):
#         return self.id
