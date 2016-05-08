# coding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    owner = models.ForeignKey(User,verbose_name=u'作者')
    avatar = models.CharField(u'图像',max_length=300,blank=True)
    title = models.CharField(u"标题",max_length=100)
    content = models.CharField(u"内容",max_length=100000)
    status = models.IntegerField(u"状态",choices=((0,u'普通'),(-1,u'删除'),(10,'精华')),default=0)

    create_timestamp = models.DateTimeField(u'创建时间',auto_now_add=True)
    last_update_timestamp = models.DateTimeField(u'更新时间',auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'产品'
        verbose_name_plural = u'产品'

