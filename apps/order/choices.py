from django.db import models


class Status(models.IntegerChoices):
    """ 生产进度 """
    STATUS_BL = 1, '备料'
    STATUS_PD = 2, '配单'
    STATUS_DSC = 3, '待生产'
    STATUS_SCZ = 4, '生产中'
    STATUS_SCWC = 5, '生产完成'
    STATUS_WLSC = 6, '物流上传'
    STATUS_DDWC = 7, '订单完成'
