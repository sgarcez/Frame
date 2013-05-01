from django import forms
from comps.models import Device


class CompForm(forms.Form):
    device = forms.ModelChoiceField(required=True, queryset=Device.objects.all(), empty_label="select a device", widget=forms.Select())
    image = forms.ImageField(required=True)
