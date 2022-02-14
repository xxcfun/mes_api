from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    """ 用户信息 """
    name = models.CharField('姓名', max_length=16, null=True, blank=True)
    mobile = models.CharField('电话', max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = '用户基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class RoleProfile(models.Model):
    """ 角色信息 """
    name = models.CharField('角色名称', max_length=16)

    class Meta:
        verbose_name = '角色基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class PermissionProfile(models.Model):
    """ 权限功能 """
    name = models.CharField('权限名称', max_length=64)
    url = models.CharField('url链接', max_length=128)

    class Meta:
        verbose_name = '权限基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserToRoleRelation(models.Model):
    """ 用户角色关系表 """
    user = models.ManyToManyField(UserProfile, verbose_name='用户id')
    role = models.ManyToManyField(RoleProfile, verbose_name='角色id')

    class Meta:
        verbose_name = '用户角色关系表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user


class RoleToPermissionRelation(models.Model):
    """ 角色权限关系表 """
    role = models.ManyToManyField(RoleProfile, verbose_name='角色id')
    permission = models.ManyToManyField(PermissionProfile, verbose_name='权限id')

    class Meta:
        verbose_name = '角色权限关系表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.role

