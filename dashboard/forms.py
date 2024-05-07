from django import forms
from .models import FoodStyle, Country, Food, Gender, Generation, Area, RespAcq, Respondent, FoodCat

class FilterForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=False, label="Country")
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(), required=False, label="Gender")
    generation = forms.ModelChoiceField(queryset=Generation.objects.all(), required=False, label="Generation")
    resp_acq = forms.ModelChoiceField(queryset=RespAcq.objects.all(), required=False, label="Responsible for Purchases")
    #foodstyle = forms.ModelChoiceField(queryset=FoodStyle.objects.all(), required=False, label="Food Style")
