from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.db.models import Q
from .models import *
from .forms import *
# Create your views here.
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


def homeView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('manager:login'))
    else:
        return render(request, "manager/home.html")

class MyPagiantor():
    def get_context_data(self, **kwargs):
        """
        在视图函数中将模板变量传递给模板是通过给 render 函数的 context 参数传递一个字典实现的，
        例如 render(request, 'blog/index.html', context={'post_list': post_list})，
        这里传递了一个 {'post_list': post_list} 字典给模板。
        在类视图中，这个需要传递的模板变量字典是通过 get_context_data 获得的，
        所以我们复写该方法，以便我们能够自己再插入一些我们自定义的模板变量进去。
        """

        # 首先获得父类生成的传递给模板的字典。
        context = super().get_context_data(**kwargs)

        # 父类生成的字典中已有 paginator、page_obj、is_paginated 这三个模板变量，
        # paginator 是 Paginator 的一个实例，
        # page_obj 是 Page 的一个实例，
        # is_paginated 是一个布尔变量，用于指示是否已分页。
        # 例如如果规定每页 10 个数据，而本身只有 5 个数据，其实就用不着分页，此时 is_paginated=False。
        # 关于什么是 Paginator，Page 类在 Django Pagination 简单分页：http://zmrenwu.com/post/34/ 中已有详细说明。
        # 由于 context 是一个字典，所以调用 get 方法从中取出某个键对应的值。
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        # 调用自己写的 pagination_data 方法获得显示分页导航条需要的数据，见下方。
        pagination_data = self.pagination_data(paginator, page, is_paginated)

        # 将分页导航条的模板变量更新到 context 中，注意 pagination_data 方法返回的也是一个字典。
        context.update(pagination_data)

        # 将更新后的 context 返回，以便 ListView 使用这个字典中的模板变量去渲染模板。
        # 注意此时 context 字典中已有了显示分页导航条所需的数据。
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            # 如果没有分页，则无需显示分页导航条，不用任何分页导航条的数据，因此返回一个空的字典
            return {}

        # 当前页左边连续的页码号，初始值为空
        left = []

        # 当前页右边连续的页码号，初始值为空
        right = []

        # 标示第 1 页页码后是否需要显示省略号
        left_has_more = False

        # 标示最后一页页码前是否需要显示省略号
        right_has_more = False

        # 标示是否需要显示第 1 页的页码号。
        # 因为如果当前页左边的连续页码号中已经含有第 1 页的页码号，此时就无需再显示第 1 页的页码号，
        # 其它情况下第一页的页码是始终需要显示的。
        # 初始值为 False
        first = False

        # 标示是否需要显示最后一页的页码号。
        # 需要此指示变量的理由和上面相同。
        last = False

        # 获得用户当前请求的页码号
        page_number = page.number

        # 获得分页后的总页数
        total_pages = paginator.num_pages

        # 获得整个分页页码列表，比如分了四页，那么就是 [1, 2, 3, 4]
        page_range = paginator.page_range

        if page_number == 1:
            # 如果用户请求的是第一页的数据，那么当前页左边的不需要数据，因此 left=[]（已默认为空）。
            # 此时只要获取当前页右边的连续页码号，
            # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 right = [2, 3]。
            # 注意这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
            right = page_range[page_number:page_number + 2]

            # 如果最右边的页码号比最后一页的页码号减去 1 还要小，
            # 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示。
            if right[-1] < total_pages - 1:
                right_has_more = True

            # 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
            # 所以需要显示最后一页的页码号，通过 last 来指示
            if right[-1] < total_pages:
                last = True

        elif page_number == total_pages:
            # 如果用户请求的是最后一页的数据，那么当前页右边就不需要数据，因此 right=[]（已默认为空），
            # 此时只要获取当前页左边的连续页码号。
            # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 left = [2, 3]
            # 这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]

            # 如果最左边的页码号比第 2 页页码号还大，
            # 说明最左边的页码号和第 1 页的页码号之间还有其它页码，因此需要显示省略号，通过 left_has_more 来指示。
            if left[0] > 2:
                left_has_more = True

            # 如果最左边的页码号比第 1 页的页码号大，说明当前页左边的连续页码号中不包含第一页的页码，
            # 所以需要显示第一页的页码号，通过 first 来指示
            if left[0] > 1:
                first = True
        else:
            # 用户请求的既不是最后一页，也不是第 1 页，则需要获取当前页左右两边的连续页码号，
            # 这里只获取了当前页码前后连续两个页码，你可以更改这个数字以获取更多页码。
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]

            # 是否需要显示最后一页和最后一页前的省略号
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True

            # 是否需要显示第 1 页和第 1 页后的省略号
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
        'left': left,
        'right': right,
        'left_has_more': left_has_more,
        'right_has_more': right_has_more,
        'first': first,
        'last': last,
        }

        return data    


@method_decorator(login_required(login_url=('/manager/login')), name='dispatch')
class DeviceIndexView(generic.ListView):
    model = equipment
    context_object_name = 'device_list'
    template_name = 'manager/indexDevice.html'
    paginate_by = 20
    ordering = 'id'
    district = 0
    mean = 0
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['districts'] = district.objects.all()
        context['measure_means'] = measure_means.objects.all()
        return context
    
    def get_queryset(self):
        filter_dict = self.request.GET.dict()
        print('filter:'+str(filter_dict))
        if 'csrfmiddlewaretoken' in filter_dict.keys():
            filter_dict.pop('csrfmiddlewaretoken')
        if 'page' in filter_dict.keys():
            filter_dict.pop('page')
        if 'search_word' in filter_dict.keys():
            search_word = filter_dict['search_word']
            filter_dict.pop('search_word')
            queryset = self.model.objects.filter(**filter_dict).filter(Q(name_cn__icontains=search_word))
        else:
            queryset = self.model.objects.filter(**filter_dict)
        return queryset    


@login_required(login_url=('/manager/login'))
def newDeviceRecord(request):
    form = DeviceDetailForm()
    if request.method == 'POST':
        form = DeviceDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('1')
        else:
            return HttpResponse('2')
    else:
        return render(request,'manager/newRecord.html', {'form':form,'par':'deviceIndex'})

@login_required(login_url=('/manager/login'))
def deviceDetailView(request, pk):
    record = get_object_or_404(equipment,pk=pk)    
    if pk and request.method=='GET':
        form = DeviceDetailForm(instance=record)
    elif request.method=='POST':
        form = DeviceDetailForm(request.POST, request.FILES, instance=record)
        print(request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('image')
            for f in files:
                fw = open(f.name,'wb+')
                for chunk in f.chunks():
                    fw.write(chunk)
                fw.close()
            form.save()
            #return redirect(reverse('manager:stationIndex'))
            return HttpResponse("1")
        else:
            return HttpResponse("2")
    else:
        form = DeviceDetailForm()
    print(pk)
    return render(request, 'manager/detail.html', {'form':form, 'pk':pk})



@login_required(login_url=('/manager/login'))
def deleteDeviceView(request, pk):
    if equipment.objects.get(pk=pk).delete():
        return HttpResponse("1")
    else:
        return HttpResponse("2")


@method_decorator(login_required(login_url=('/manager/login')), name='dispatch')
class DeleveryIndexView(generic.ListView):
    model = equip_delivery_record
    context_object_name = 'delevery_list'
    template_name = 'manager/indexDelevery.html'
    paginate_by = 20
    ordering = '-send_date'
    district = 0
    mean = 0
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['districts'] = district.objects.all()
        context['measure_means'] = measure_means.objects.all()
        return context
    
    def get_queryset(self):
        filter_dict = self.request.GET.dict()
        print('filter:'+str(filter_dict))
        if 'csrfmiddlewaretoken' in filter_dict.keys():
            filter_dict.pop('csrfmiddlewaretoken')
        if 'page' in filter_dict.keys():
            filter_dict.pop('page')
        if 'search_word' in filter_dict.keys():
            search_word = filter_dict['search_word']
            filter_dict.pop('search_word')
            queryset = self.model.objects.filter(**filter_dict).filter(Q(receiver_unit__icontains=search_word))
        else:
            queryset = self.model.objects.filter(**filter_dict)
        return queryset    

@login_required(login_url=('/manager/login'))
def newDeleveryRecord(request):
    form = DeleveryDetailForm()
    if request.method == 'POST':
        form = DeleveryDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('1')
        else:
            return HttpResponse('2')
    else:
        return render(request,'manager/newRecord.html', {'form':form,'par':'deleveryIndex'})

@login_required(login_url=('/manager/login'))
def deleveryDetailView(request, pk):
    record = get_object_or_404(equip_delivery_record,pk=pk)
    if pk and request.method=='GET':
        form = DeleveryDetailForm(instance=record)
    elif request.method=='POST':
        form = DeleveryDetailForm(request.POST, request.FILES, instance=record)
        print(request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('image')
            for f in files:
                fw = open(f.name,'wb+')
                for chunk in f.chunks():
                    fw.write(chunk)
                fw.close()
            form.save()
            #return redirect(reverse('manager:stationIndex'))
            return HttpResponse("1")
        else:
            return HttpResponse("2")
    else:
        form = DeleveryDetailForm()
    print(pk)
    return render(request, 'manager/detail.html', {'form':form, 'pk':pk})


@login_required(login_url=('/manager/login'))
def deleteDeleveryView(request, pk):
    if equip_delivery_record.objects.get(pk=pk).delete():
        return HttpResponse("1")
    else:
        return HttpResponse("2")

@method_decorator(login_required(login_url=('/manager/login')), name='dispatch')
class StationIndexView(generic.ListView):
    model = station
    context_object_name = 'station_list'
    template_name = 'manager/indexStation.html'
    paginate_by = 20
    ordering = ['district','name_cn']
    district = 0
    mean = 0
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['districts'] = dict(DISTRICT_CHOICE)
        context['districts'] = district.objects.all()
        #context['measure_means'] = dict(MEASURE_MEANS_CHOICE)
        context['measure_means'] = measure_means.objects.all()
        return context
    
    def get_queryset(self):
        filter_dict = self.request.GET.dict()
        print('filter:'+str(filter_dict))
        if 'csrfmiddlewaretoken' in filter_dict.keys():
            filter_dict.pop('csrfmiddlewaretoken')
        if 'page' in filter_dict.keys():
            filter_dict.pop('page')
        if 'search_word' in filter_dict.keys():
            search_word = filter_dict['search_word']
            filter_dict.pop('search_word')
            queryset = self.model.objects.filter(**filter_dict).filter(Q(name_cn__icontains=search_word))
        else:
            queryset = self.model.objects.filter(**filter_dict)
        return queryset

@login_required(login_url=('/manager/login'))
def newStationRecord(request):
    form = StationDetailForm()
    if request.method == 'POST':
        form = StationDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('1')
        else:
            return HttpResponse('2')
    else:
        return render(request,'manager/newRecord.html', {'form':form,'par':'stationIndex'})

@login_required(login_url=('/manager/login'))
def stationDetailView(request, pk):
    record = get_object_or_404(station,pk=pk)    
    if pk and request.method=='GET':
        form = StationDetailForm(instance=record)
    elif request.method=='POST':
        form = StationDetailForm(request.POST, request.FILES, instance=record)
        print(request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('image')
            for f in files:
                fw = open(f.name,'wb+')
                for chunk in f.chunks():
                    fw.write(chunk)
                fw.close()
            form.save()
            #return redirect(reverse('manager:stationIndex'))
            return HttpResponse("1")
        else:
            return HttpResponse("2")
    else:
        form = StationDetailForm()
    return render(request, 'manager/detail.html', {'form':form, 'pk':pk})

@login_required(login_url=('/manager/login'))
def deleteStationView(request, pk):
    if station.objects.get(pk=pk).delete():
        return HttpResponse('1')
    else:
        return HttpResponse('2')

@method_decorator(login_required(login_url=('/manager/login')), name='dispatch')
class EquipStatusIndexView(generic.ListView):
    model = equip_status
    context_object_name = 'equip_status_list'
    template_name = 'manager/indexEquipStatus.html'
    paginate_by = 20
    ordering = ['station','equipment']
    district = 0
    mean = 0
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['districts'] = district.objects.all()
        context['measure_means'] = measure_means.objects.all()
        return context
    
    def get_queryset(self):
        filter_dict = self.request.GET.dict()
        print('filter:'+str(filter_dict))
        if 'csrfmiddlewaretoken' in filter_dict.keys():
            filter_dict.pop('csrfmiddlewaretoken')
        if 'page' in filter_dict.keys():
            filter_dict.pop('page')
        if 'search_word' in filter_dict.keys():
            search_word = filter_dict['search_word']
            filter_dict.pop('search_word')
            queryset = self.model.objects.filter(**filter_dict).filter(Q(equip_status__icontains=search_word))
        else:
            queryset = self.model.objects.filter(**filter_dict)
        return queryset

@login_required(login_url=('/manager/login'))
def neweEquipStatusRecord(request):
    form = EquipStatusForm()
    if request.method == 'POST':
        form = EquipStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('1')
        else:
            return HttpResponse('2')
    else:
        return render(request,'manager/newRecord.html', {'form':form,'par':'equipStatusIndex'})

@login_required(login_url=('/manager/login'))
def equipStatusDetailView(request, pk):
    record = get_object_or_404(equip_status,pk=pk)    
    if pk and request.method=='GET':
        form = EquipStatusForm(instance=record)
    elif request.method=='POST':
        form = EquipStatusForm(request.POST, request.FILES, instance=record)
        print(request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('image')
            for f in files:
                fw = open(f.name,'wb+')
                for chunk in f.chunks():
                    fw.write(chunk)
                fw.close()
            form.save()
            #return redirect(reverse('manager:stationIndex'))
            return HttpResponse("1")
        else:
            return HttpResponse("2")
    else:
        form = EquipStatusForm()
    return render(request, 'manager/detail.html', {'form':form, 'pk':pk})

@login_required(login_url=('/manager/login'))
def deleteEquipStatusView(request, pk):
    if equip_status.objects.get(pk=pk).delete():
        return HttpResponse('1')
    else:
        return HttpResponse('2')



@method_decorator(login_required(login_url=('/manager/login')), name='dispatch')
class EquipMaintainIndexView(generic.ListView):
    model = equip_maintain_record
    context_object_name = 'equip_maintain_list'
    template_name = 'manager/indexEquipMaintain.html'
    paginate_by = 20
    ordering = ['station','equipment']
    district = 0
    mean = 0
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['districts'] = district.objects.all()
        context['measure_means'] = measure_means.objects.all()
        return context
    
    def get_queryset(self):
        filter_dict = self.request.GET.dict()
        print('filter:'+str(filter_dict))
        if 'csrfmiddlewaretoken' in filter_dict.keys():
            filter_dict.pop('csrfmiddlewaretoken')
        if 'page' in filter_dict.keys():
            filter_dict.pop('page')
        if 'search_word' in filter_dict.keys():
            search_word = filter_dict['search_word']
            filter_dict.pop('search_word')
            queryset = self.model.objects.filter(**filter_dict).filter(Q(equip_maintain_record__icontains=search_word))
        else:
            queryset = self.model.objects.filter(**filter_dict)
        return queryset

@login_required(login_url=('/manager/login'))
def newEquipMaintainRecord(request):
    form = EquipMaintainForm()
    if request.method == 'POST':
        form = EquipMaintainForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('1')
        else:
            return HttpResponse('2')
    else:
        return render(request,'manager/newRecord.html', {'form':form,'par':'equipMaintainIndex'})

@login_required(login_url=('/manager/login'))
def equipMaintainDetailView(request, pk):
    record = get_object_or_404(equip_maintain_record,pk=pk)    
    if pk and request.method=='GET':
        form = EquipMaintainForm(instance=record)
    elif request.method=='POST':
        form = EquipMaintainForm(request.POST, request.FILES, instance=record)
        print(request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('image')
            for f in files:
                fw = open(f.name,'wb+')
                for chunk in f.chunks():
                    fw.write(chunk)
                fw.close()
            form.save()
            #return redirect(reverse('manager:stationIndex'))
            return HttpResponse("1")
        else:
            return HttpResponse("2")
    else:
        form = EquipMaintainForm()
    return render(request, 'manager/detail.html', {'form':form, 'pk':pk})

@login_required(login_url=('/manager/login'))
def deleteEquipMaintainView(request, pk):
    if equip_maintain_record.objects.get(pk=pk).delete():
        return HttpResponse('1')
    else:
        return HttpResponse('2')
