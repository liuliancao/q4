from django.db import models

# Create your models here.
class Purchase(models.Model):
    applicant = models.CharField(max_length=50) 
    product = models.CharField(max_length=50)
    idc = models.CharField(max_length=50)
    cost_centre = models.CharField(max_length=50)
    ticket = models.CharField(max_length=50)
    apply_type = models.CharField(max_length=10,choices=apply_choices,help_text='申请类型')
    allocation = models.CharField(max_length=150,help_text='配置')
    number = models.IntegerField(help_text='数量')
    cmdb_type = models.CharField(max_length=150,help_text='BIH|HIH')
    cmdb_from = models.IntegerField(help_text='资产编号头')
    cmdb_to = models.IntegerField(help_text='资产编号尾')
    reason = models.CharField(max_length=333,help_text='申请理由')
    desc = models.CharField(max_length=333,help_text='备注')
    state = models.CharField(max_length=10,choices=purchase_choices)
    
    
    apply_choices = (
        ('0','服务器‘),
        ('1',’其他配件')
    )

    purchase_choices = (
        ('0','未到货‘),
        ('1',’预计到货'),
        ('2','安装需求发出')
    )

    def __str__(self):
        ret = '[' + self.idc + ']'+ self.cost_centre + '-' +  self.product + '(' + self.applicant ')'
        return ret



class Host(models.Model):
    purchase = models.ForeignKey(Purchase, help_text='经手人')
    hostname = models.CharField(max_length=50)
    cmdb_number = IntegerField(help_text='资产编号')
    ip = models.CharField(max_length=20, blank=True, null=True)
    ins_requirement = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    state = models.CharField(max_length=10,choices=host_choices)

    host_choices = (
        ('0','已经安装'),
        ('1','sa初始化完毕'),
        ('2','已经交付')
    )

    def __str__(self):
        ret = self.ip
        return ret
