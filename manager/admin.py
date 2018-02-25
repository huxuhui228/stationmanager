#from django.contrib import admin
#from .models import *
## Register your models here.

#admin.site.register(
    #(equip_maintain_record, district, measure_means)
#)

#class EquipInline(admin.TabularInline):
    #model = equip_status
    #fields = ('equipment','ip_address','ip_mask','ip_gateway','sampling_rate','transmission_type','install_date')
    #extra = 1

#@admin.register(station)
#class StationAdmin(admin.ModelAdmin):
    #list_display = ('name_cn','name_en','code','district','measure_means','longtitude','latitude','heigh')
    #list_display_links = ('name_cn','name_en','code')
    #list_filter = ['district','measure_means','project_source']
    #ordering = ('district','name_cn',)
    #search_fields = ['name_cn','name_cn']
    #data_hierarchy = 'district'
    #inlines = [EquipInline]

#@admin.register(equip_status)
#class Equip_statusAdmin(admin.ModelAdmin):
    #list_display = ('station','equipment','ip_address','sampling_rate','transmission_type','install_date','remove_date')
    #list_filter = ['station__district']
    #search_fields = ['station__name_cn','equipment__serial_num']
    #data_hierarchy = 'station__district'
    

#@admin.register(equipment)
#class EquipmentAdmin(admin.ModelAdmin):
    #list_display = ('equip_type','serial_num')

#@admin.register(equip_manu)
#class Equip_manuAdmin(admin.ModelAdmin):
    #list_display = ('name','staff_name','address','phone','mobile_phone')
    #ordering = ('name',)
    #search_fields = ['name','staff_name','address','phone']

#@admin.register(equip_type)
#class Equip_typeAdmin(admin.ModelAdmin):
    #list_display = ('model','name','manufacture')
    #ordering = ('model',)

#class HasReturnedFilter(admin.SimpleListFilter):
    #title = (u'是否已经返回')

    ## Parameter for the filter that will be used in the URL query.
    #parameter_name = 'has_returned'

    #def lookups(self, request, model_admin):
        #"""
        #Returns a list of tuples. The first element in each
        #tuple is the coded value for the option that will
        #appear in the URL query. The second element is the
        #human-readable name for the option that will appear
        #in the right sidebar.
        #"""
        #return (
            #(0, u'无需返回'),
            #(1, u'已返回'),
            #(2, u'未返回'),
        #)

    #def queryset(self, request, queryset):
        #"""
        #Returns the filtered queryset based on the value
        #provided in the query string and retrievable via
        #`self.value()`.
        #"""
        #if self.value():
            #if int(self.value()) == 0:
                #return queryset.filter(need_back=False)
            #if int(self.value()) == 1:
                #return queryset.filter(back_receiver__isnull=False) & queryset.filter(back_date__isnull=False)
            #if int(self.value()) == 2:
                #return queryset.filter(back_receiver__isnull=True) & queryset.filter(back_date__isnull=True) & queryset.filter(need_back=True)


#@admin.register(equip_delivery_record)
#class Equip_delivery_recordAdmin(admin.ModelAdmin):
    #def has_returned(self,obj):
        #if obj.back_status == '无需返回':
            #return u'<span style="color:green;font-weight:bold">%s</span>' % (u"无需返回")
        #else:
            #if obj.back_status == '未返回':
                #return u'<span style="color:red;font-weight:bold">%s</span>' % (u"未返回")
            #else:
                #if obj.back_status == '已返回':
                    #return u'<span style="color:blue;font-weight:bold">%s</span>' % (u"已返回")
                #else:
                    #if obj.back_status == '部分返回':
                        #return u'<span style="color:black;font-weight:bold">%s</span>' % (u"部分返回")

    #has_returned.short_description = u'返回状态'
    #has_returned.allow_tags = True
    #list_display = ('send_equip_type','serial_num','send_date','sender',
                    #'receiver','receiver_unit','back_equip_type','back_serial_num',
                    #'back_unit','back_sender','back_date','note','has_returned')
    #ordering = ('-send_date','-back_date')
    #search_fields = ['send_equip_type__model','serial_num',
                    #'receiver','receiver_unit','back_equip_type__model',
                    #'back_serial_num','back_unit','back_sender','note']
    #list_filter = ('back_status',)
    #list_display_links = ('send_equip_type','back_equip_type')
    #fieldsets = [
            #(u'寄出信息',{'fields':['send_equip_type','serial_num','number',
                #'send_date','sender','receiver_unit','receiver','back_status']}),
            #(u'寄回信息',{'fields':['back_equip_type','back_serial_num',
                #'back_unit','back_sender','back_receiver','back_date']}),
            #(None,{'fields':['charge','note']})
            #]


#@admin.register(station_maintain_record)
#class Station_maintain_recordAdmin(admin.ModelAdmin):
    #list_display = ('district','station','intro','report_date','reporter','fault_startdate','fault_enddate','staff','maintain_process')
    #fields = ('district','station','equip','intro','report_date','reporter','fault_startdate','fault_enddate','staff','maintain_process','note')
    #ordering = ('-fault_startdate','station')
    #list_filter = ('district',)
    #search_fields = ('district','station','intro','staff','maintain_process')
    #list_display_links = ('district','station','intro',)

#@admin.register(schedule)
#class ScheduleAdmin(admin.ModelAdmin):
    #list_display = ('plan_time','to_do_time','staff','plan','status')
    #list_filter = ('status',)