from django.forms import ModelForm,ClearableFileInput,DateInput,SelectDateWidget,TextInput
import datetime
from .models import *

class DeleveryDetailForm(ModelForm):
    class Meta:
        model = equip_delivery_record
        fields = '__all__'
        widgets = {
            "send_date": SelectDateWidget(years=range(2016,datetime.date.today().year+1),
                                          months={i:i for i in range(1,13)}),
            "back_date": SelectDateWidget(years=range(2016,datetime.date.today().year+1),
                                          months={i:i for i in range(1,13)}),
        }

class DeviceDetailForm(ModelForm):
    class Meta:
        model = equipment
        fields = '__all__'

class StationDetailForm(ModelForm):
    class Meta:
        model = station
        fields = '__all__'
        widgets = {
                "image": ClearableFileInput(attrs={'multiple': True}),
            }

class EquipStatusForm(ModelForm):
    class Meta:
        model = equip_status
        fields = '__all__'

class EquipMaintainForm(ModelForm):
    class Meta:
        model = equip_maintain_record
        fields = '__all__'
