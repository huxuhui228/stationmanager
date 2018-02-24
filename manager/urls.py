from django.urls import path
from django.contrib.auth.views import login,logout
from . import views

app_name = "manager"
urlpatterns = [
	path(r'', views.homeView, name='home'),
        path(r'login/', login, {'template_name':'manager/login.html'}, name='login'),
        path(r'logout/', logout, {'template_name':'manager/login.html'}, name='logout'),
        
        path(r'deviceIndex/', views.DeviceIndexView.as_view(), name='deviceIndex'),
        path(r'deviceIndex/new',views.newDeviceRecord, name='newDeviceRecord'),
        path(r'deviceIndex/<int:pk>', views.deviceDetailView, name='deviceDetail'),
        path(r'deviceIndex/<int:pk>/delete', views.deleteDeviceView, name='deleteDevice'),
        
        path(r'deleveryIndex/', views.DeleveryIndexView.as_view(), name='deleveryIndex'),     
        path(r'deleveryIndex/new', views.newDeleveryRecord, name='newDeleveryRecord'),
        path(r'deleveryIndex/<int:pk>', views.deleveryDetailView, name='deleveryDetail'),
        path(r'deleveryIndex/<int:pk>/delete', views.deleteDeleveryView, name='deleteDelevery'),
        
        path(r'stationIndex/', views.StationIndexView.as_view(), name='stationIndex'),     
        path(r'stationIndex/new', views.newStationRecord, name='newStationRecord'),
        path(r'stationIndex/<int:pk>', views.stationDetailView, name='stationDetail'),
        path(r'stationIndex/<int:pk>/delete', views.deleteStationView, name='deleteStation'), 
        
        path(r'equipStatusIndex/', views.EquipStatusIndexView.as_view(), name='equipStatusIndex'),     
        path(r'equipStatusIndex/new', views.neweEquipStatusRecord, name='newEquipStatusRecord'),
        path(r'equipStatusIndex/<int:pk>', views.equipStatusDetailView, name='equipStatusDetail'),
        path(r'equipStatusIndex/<int:pk>/delete', views.deleteEquipStatusView, name='deleteEquipStatus'),   
        
        path(r'equipMaintainIndex/', views.EquipMaintainIndexView.as_view(), name='equipMaintainIndex'),     
        path(r'equipMaintainIndex/new', views.neweEquipMaintainRecord, name='newEquipMaintainRecord'),
        path(r'equipMaintainIndex/<int:pk>', views.equipMaintainDetailView, name='equipMaintainDetail'),
        path(r'equipMaintainIndex/<int:pk>/delete', views.deleteEquipMaintainView, name='deleteEquipMaintain'),          
	]