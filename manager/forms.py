from django.forms import ModelForm,ClearableFileInput
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
        widgets = {
                "image": ClearableFileInput(attrs={'multiple': True}),
            }