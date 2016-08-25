# -*- coding: utf-8
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    #name = models.CharField(max_length=128,verbose_name=u'用户名')
    #email = models.CharField(max_length=32)
    pass_field = models.CharField(db_column='pass', max_length=16)
    passwd = models.CharField(max_length=16)
    t = models.IntegerField(default='0')
    u = models.BigIntegerField(default='0')
    d = models.BigIntegerField(default='0')
    transfer_enable = models.BigIntegerField(default='0')
    port = models.IntegerField(default='10000')
    switch = models.IntegerField(default='0')
    enable = models.IntegerField(default='0')
    type = models.IntegerField(default='0')
    last_get_gift_time = models.IntegerField(default='0')
    last_rest_pass_time = models.IntegerField(default='0')

    #Django如何自定义表名
    class Meta:
        db_table = 'user'
        verbose_name_plural = verbose_name = u'ss用户'

    def __unicode__(self):
        return self.email

class Node(models.Model):
    node_name = models.CharField(max_length=128,verbose_name=u'服务器名')
    node_type = models.IntegerField(verbose_name=u'类型')
    node_ip = models.CharField(max_length=128,verbose_name=u'ip')
    node_method = models.CharField(max_length=64,verbose_name=u'加密码方式')
    node_info = models.CharField(max_length=128,verbose_name=u'信息')
    node_status = models.CharField(max_length=128,verbose_name=u'状态')
    node_order = models.IntegerField(verbose_name=u'排序')

    class Meta:
        verbose_name_plural = verbose_name = u'代理节点'
    # managed = False
    #   db_table = 'ssnode'

    def __unicode__(self):
        return self.node_name



class Product(models.Model):
    product_name = models.CharField(max_length=128,  verbose_name=u'产品名称')
    description = models.TextField( verbose_name=u'产品说明')
    price = models.DecimalField(max_digits=8,decimal_places=2,verbose_name=u'价格')
    date_available = models.DateField(verbose_name=u'时间')

    class Meta:
        verbose_name_plural = verbose_name = u'产品'

    def __unicode__(self):
        return self.product_name

class Prder(models.Model):
    order_number = models.CharField(max_length=128, verbose_name=u'订单号')
    order_user = models.ForeignKey(User,verbose_name=u'对应用户')
    order_product = models.ForeignKey(Product,verbose_name=u'对应产品')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    activate = models.CharField(max_length=128,default='no' ,verbose_name=u'是否已付款')

    class Meta:
        verbose_name_plural = verbose_name = u'订单'

    def __unicode__(self):
        return self.order_number

