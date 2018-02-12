from django.forms import ModelForm
from .models import *
class DeleveryDetailForm(ModelForm):
    class Meta:
        model = equip_delivery_record
        fields = '__all__'

class DeviceDetailForm(ModelForm):
    class Meta:
        model = equipment
        fields = '__all__'

class StationDetailForm(ModelForm):
    class Meta:
        model = station
        fields = '__all__'