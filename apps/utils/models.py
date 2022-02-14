from django.db import models


class CommonModel(models.Model):
    """ 模型公共基础类 """
    is_valid = models.BooleanField('是否有效', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
