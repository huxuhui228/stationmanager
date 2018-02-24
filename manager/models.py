#!coding:utf-8
from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.
PROCECT_CHOICE = (
    ('十五','十五'),('十一五','十一五'),('十二五','十二五'),('背景场','背景场'),('十三五','十三五'),('九五','九五'),
    )
DISTRICT_CHOICE = (
    ('济南','济南'),('泰安','泰安'),('潍坊','潍坊'),('德州','德州'),
    ('滨州','滨州'),('莱芜','莱芜'),('青岛','青岛'),('烟台','烟台'),
    ('日照','日照'),('东营','东营'),('济宁','济宁'),('菏泽','菏泽'),
    ('聊城','聊城'),('临沂','临沂'),('枣庄','枣庄'),('淄博','淄博'),
    ('威海','威海'),('省局','省局'),
    )
MEASURE_MEANS_CHOICE = (
    ('测震','测震'),('强震','强震'),
    ('前兆','前兆')
    )
SENDER_CHOICES = (
    ('胡旭辉','胡旭辉'),('李小晗','李小晗'),('王杰民','王杰民'),('曲利','曲利'),
    ('冯志军','冯志军'),('马丕峰','马丕峰'),('王忠民','王忠民'),('吴双','吴双')
    )
BACK_STATUS = (
    ('未返回','未返回'),('已返回','已返回'),('部分返回','部分返回'),('无需返回','无需返回')
    )
STATUS_CHOICE = (
    ('1','台上正常使用'),
    ('2','在库'),
    ('3','在修'),
    )
SAMPLING_RATE_CHOICE = (
    ('100sps','每秒100点'),
    ('200sps','每秒200点'),
    ('50sps','每秒50点'),
    ('1spm','每分1点'),
    ('1sph','每小时1点')
    )
TRANSMISSION_TYPE_CHOICE = (
    ('SDH','SDH'),
    ('3G','3G'),
    ('Internet_VPN','Internet_VPN'),
    ('电台','电台')
    )
SCHEDULE_status_CHOICE = (
    ('1','未完成'),
    ('2','已完成'),
    ('3','已放弃'),
    )


class district(models.Model):
    district = models.CharField(max_length=32, default='', blank=True)
    class Meta:
        verbose_name = 'district'
    def __str__(self):
        return self.district

class measure_means(models.Model):
    means = models.CharField(max_length=32, default='', blank=True)

    def __str__(self):
        return self.means

class image(models.Model):
    belong_to = models.ForeignKey('station', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'station_img/')
    

class station(models.Model):

    code = models.CharField(max_length=32,default='',blank=True)
    name_en = models.CharField(max_length=64,default='',null=True,blank=True)
    name_cn = models.CharField(max_length=64)
    measure_means = models.ForeignKey('measure_means', on_delete=models.CASCADE,null=True,blank=True)
    #measure_means = models.CharField(max_length=32,choices=MEASURE_MEANS_CHOICE,
                                     #default='测震',blank=True)    
    project_source = models.CharField(max_length=32,blank=True,
                    default='十五',choices=PROCECT_CHOICE)

    #district = models.CharField(max_length=32,choices=DISTRICT_CHOICE,default='济南')
    district = models.ForeignKey('district', on_delete=models.CASCADE,null=True,blank=True)
    longtitude = models.FloatField(default=None,null=True,blank=True)
    latitude = models.FloatField(default=None,null=True,blank=True)
    heigh = models.FloatField(default=None,null=True,blank=True)
    lithology = models.CharField(max_length=32,default='',blank=True)
    address = models.CharField(max_length=256,default='',blank=True)
    staff_name = models.CharField(max_length=32,default='',blank=True)
    phone = models.CharField(max_length=32,default='',blank=True)
    note = models.TextField(max_length=256,blank=True)

    class Meta:
        verbose_name = '台站列表'
        verbose_name_plural = '台站列表'
    def __str__(self):
        return self.name_cn



class equip_manu(models.Model):
    name = models.CharField(max_length=128)
    staff_name = models.CharField(max_length=32,blank=True)
    address = models.CharField(max_length=128,blank=True)
    phone = models.CharField(max_length=128,blank=True)
    mobile_phone = models.CharField(max_length=128,blank=True)
    emai_address = models.EmailField(max_length=128,blank=True)
    note = models.TextField(max_length=256,default='',blank=True)

    class Meta:
        verbose_name = '设备生产厂家'
        verbose_name_plural = '设备生产厂家'
    def __str__(self):
        return self.name + '-' + self.staff_name

class equip_type(models.Model):
    model = models.CharField(max_length=32,blank=True)
    name = models.CharField(max_length=32,blank=True)
    manufacture = models.ForeignKey('equip_manu',on_delete=models.CASCADE,null=True,blank=True)
    note = models.TextField(max_length=256,default='',blank=True)

    class Meta:
        verbose_name = '设备类型'
        verbose_name_plural = '设备类型'
        ordering = ["model"]
    def __str__(self):
        return self.model

class equipment(models.Model):

    equip_type = models.ForeignKey('equip_type',on_delete=models.CASCADE) 
    serial_num = models.CharField(max_length=64,blank=True)
    station = models.ForeignKey('station',on_delete=models.CASCADE)
    note = models.TextField(max_length=256,default='',blank=True)

    class Meta:
        verbose_name = '设备列表'
        verbose_name_plural = '设备列表'
    def __str__(self):
        return self.equip_type.model + '_' +self.serial_num

class station_maintain_record(models.Model):
    station = models.ForeignKey('station',on_delete=models.CASCADE,verbose_name='台站')
    district = models.CharField(max_length=32,choices=DISTRICT_CHOICE,default='烟台',verbose_name='地区')
#    station = models.CharField(max_length=64,verbose_name='台站')
    #equip = models.CharField(max_length=32,null=True,blank=True,verbose_name='设备')
    equip = models.ForeignKey('equipment',on_delete=models.CASCADE,null=True,blank=True,verbose_name='设备')
    intro = models.CharField(max_length=64,blank=True,verbose_name='故障描述')
    report_date = models.DateTimeField(null=True,blank=True,verbose_name='报修时间')
    reporter = models.CharField(max_length=64,blank=True,verbose_name='报修人或发现人')
    fault_startdate = models.DateTimeField(null=True,blank=True,verbose_name='开始时间')
    fault_enddate = models.DateTimeField(null=True,blank=True,verbose_name='结束时间')
    staff = models.CharField(max_length=32,blank=True,verbose_name='处理人员')
    maintain_process = models.TextField(max_length=256,default='',blank=True,verbose_name='处理经过')
    note = models.TextField(max_length=256,default='',blank=True,verbose_name='备注')

    class Meta:
        verbose_name = '台站维修记录'
        verbose_name_plural = '台站维修记录'
    def __str__(self):
        return self.intro

class equip_maintain_record(models.Model):
    station = models.ForeignKey('station',on_delete=models.CASCADE)
    equip = models.ForeignKey('equipment',on_delete=models.CASCADE)
    intro = models.TextField(max_length=128,blank=True)
    fault_startdate = models.DateTimeField(auto_now=True,null=True,blank=True)
    fault_enddate = models.DateTimeField(auto_now=True,null=True,blank=True)
    maintain_date = models.DateTimeField(auto_now=True,null=True,blank=True)
    staff = models.CharField(max_length=32,blank=True)
    note = models.TextField(max_length=256,default='',blank=True)

    class Meta:
        verbose_name = '设备维修记录'
        verbose_name_plural = '设备维修记录'
    def __str__(self):
        return self.intro

class equip_delivery_record(models.Model):

    send_equip_type = models.ForeignKey('equip_type',null=True,blank=True,on_delete=models.CASCADE,related_name="寄出设备类型",verbose_name="寄出设备类型")
    serial_num = models.CharField(max_length=64,blank=True,verbose_name="序列号")
    number = models.IntegerField(default=1,null=True,blank=True,verbose_name="寄出数量")
    send_date = models.DateField(null=True,blank=True,verbose_name="发件时间")
    sender = models.CharField(max_length=32,choices=SENDER_CHOICES,blank=True,verbose_name="发件人")
    receiver_unit = models.CharField(max_length=32,blank=True,verbose_name="收件单位")
    receiver = models.CharField(max_length=32,blank=True,verbose_name="收件人")
    back_status = models.CharField(max_length=32,choices=BACK_STATUS,default='未返回',blank=True,verbose_name="返回状态")
    back_equip_type = models.ForeignKey('equip_type',null=True,blank=True,on_delete=models.CASCADE,related_name="寄回设备类型",verbose_name="寄回设备类型")
    back_serial_num = models.CharField(max_length=64,blank=True,verbose_name="寄回序列号")
    back_unit = models.CharField(max_length=32,blank=True,verbose_name="寄回单位")
    back_sender = models.CharField(max_length=32,blank=True,verbose_name="寄回人")
    back_receiver = models.CharField(max_length=32,choices=SENDER_CHOICES,blank=True,verbose_name="寄回接收人")
    back_date = models.DateField(null=True,blank=True,verbose_name="寄回日期")
    charge = models.FloatField(null=True,blank=True,verbose_name="维修收费")
    note = models.TextField(max_length=256,blank=True)

    class Meta:
        verbose_name = '设备寄出记录'
        verbose_name_plural = '设备寄出记录'
    def __str__(self):
        return self.send_equip_type.model if self.send_equip_type else self.back_equip_type.model

class equip_status(models.Model):

    station = models.ForeignKey(station,on_delete=models.CASCADE)
    equipment = models.ForeignKey(equipment,on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(null=True,blank=True)
    ip_mask = models.GenericIPAddressField(default='255.255.255.0',null=True,blank=True)
    ip_gateway = models.GenericIPAddressField(null=True,blank=True)
    sampling_rate = models.CharField(max_length=32,choices=SAMPLING_RATE_CHOICE,blank=True)
    transmission_type = models.CharField(max_length=32,choices=TRANSMISSION_TYPE_CHOICE,blank=True)
    install_date = models.DateField(null=True,blank=True)
    remove_date = models.DateField(null=True,blank=True)
    note = models.CharField(max_length=256,blank=True)


    class Meta:
        verbose_name = '台站设备安装情况'
        verbose_name_plural = '台站设备安装情况'
    def __str__(self):
        return self.equipment.serial_num

class trip(models.Model):
    start_date = models.DateField(verbose_name='开始时间')
    end_date = models.DateField(verbose_name='结束时间')
    place = models.CharField(max_length=32,verbose_name='出差地点')
    purpose = models.CharField(max_length=256,verbose_name='出差目的')
    staff = models.CharField(max_length=64,verbose_name='人员')

class schedule(models.Model):

    plan_time = models.DateField(verbose_name='计划发起时间',default=timezone.now)
    to_do_time = models.DateField(verbose_name='计划处理时间',null=True,blank=True)
    staff = models.CharField(max_length=32,blank=True,default='胡旭辉',verbose_name='人员')
    plan = models.TextField(max_length=256,blank=True,verbose_name='计划内容')
    status = models.CharField(max_length=32,choices=SCHEDULE_status_CHOICE,default='1',blank=True,verbose_name="完成状态")

    class Meta:
        verbose_name = '待办事件'
        verbose_name_plural = '待办事件'
    def __str__(self):
        return self.plan

