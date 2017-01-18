# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Purchase(models.Model):
    cmdb_choices = (
        ('0','BIH-H-'),
        ('1','HIH-H-')
    )

    purchase_choices = (
        ('0','未到货'),
        ('1','预计到货'),
        ('2','安装需求发出')
    )
    applicant = models.CharField(max_length=50,help_text='申请人') 
    product = models.CharField(max_length=50,help_text='产品')
    idc = models.CharField(max_length=50,help_text='机房')
    cost_centre = models.CharField(max_length=50,help_text='成本中心')
    ticket = models.CharField(max_length=50,help_text='发票抬头')
    allocation = models.CharField(max_length=150,help_text='配置')
    number = models.IntegerField(help_text='数量')
    apply_type = models.CharField(max_length=10,help_text='申请类型')
    cmdb_type = models.CharField(max_length=150,help_text='资产编号头',choices=cmdb_choices)
    cmdb_from = models.IntegerField(help_text='资产编号头')
    cmdb_to = models.IntegerField(help_text='资产编号尾')
    reason = models.CharField(max_length=333,help_text='申请理由')
    desc = models.CharField(max_length=333,help_text='备注')
    state = models.CharField(max_length=10,choices=purchase_choices,help_text='采购状态')
    
    

    def __str__(self):
        ret = '[' + self.idc + ']'+ self.cost_centre + '-' +  self.product + '(' + self.applicant + ')'
        return ret



class Host(models.Model):
    host_choices = (
        ('0','已经安装'),
        ('1','sa初始化完毕'),
        ('2','已经交付')
    )
    purchase = models.ForeignKey(Purchase, help_text='经手人')
    hostname = models.CharField(max_length=50)
    cmdb_number = models.IntegerField(help_text='资产编号')
    ip = models.CharField(max_length=20, blank=True, null=True)
    ins_requirement = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    state = models.CharField(max_length=10,choices=host_choices)


    def __str__(self):
        ret = self.ip
        return ret
