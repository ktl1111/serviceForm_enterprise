import datetime
from datetime import timedelta
from django import forms
from django.forms import ModelChoiceField
from smart_selects.form_fields import ChainedModelChoiceField

from serviceForm.models import Category, ServiceSheet, WorkState, Hospital, ContractType, MachineName, Machine, Factory, \
    Parts, Area


class CategoryForm(forms.ModelForm):
    categoryname = forms.CharField(label="類別名稱", required=True) # 資料表的欄位名稱

    class Meta:
        model = Category
        fields = ('categoryname', ) # 資料表的欄位名稱

# class HospitalForm(forms.ModelForm):
#為了讓同一個Parts class可以return不同值


class PartsgpnameModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.partsgpname


class PartsidModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.partsid


class MachineModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.machineid

# class SampleForm(forms.ModelForm):
#     class Meta:
#         model = Sample
#         fields = ('sheetid', 'hospital', 'machine')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['machine'].queryset = Machine.objects.none()

class ServiceForm(forms.ModelForm):

    options = ( ("a", "A"), ("b", "B"),)
    sheetid = forms.CharField(label='單號', widget=forms.TextInput(attrs={'class':'form-control'}))
    emp = forms.CharField(label='填表人', widget=forms.TextInput(attrs={'class':'form-control'}))
    # area = forms.ModelChoiceField(Area.objects.all(), label='地區', widget=forms.Select(attrs={'class': 'form-control', 'id': 'area'}),initial="北區")
    date = forms.DateField(label='日期', input_formats='%Y-%m-%d', widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}), initial=datetime.date.today)
    category = forms.ModelChoiceField(Category.objects.all(), label='項目總類', widget=forms.Select(attrs={'class': 'form-control'}), initial="一般維修")
    state = forms.ModelChoiceField(WorkState.objects.all(), label='狀態', widget=forms.Select(attrs={'class': 'form-control'}), initial="處理中")
    machineStop = forms.BooleanField(label='停機中', required=True)
    hospital = forms.ModelChoiceField(Hospital.objects.filter(areaid=1), label='醫院名稱', widget=forms.Select(attrs={'class': 'form-control', 'name': 'hospital', 'id':'hospital', 'onkeyup':'getdata();'}))
    receiver = forms.ModelChoiceField(Category.objects.filter(categoryname__startswith="醫用技術部"), label='收話人', widget=forms.Select(attrs={'class':'form-control'}), required=True) #要再改
    # mensent =forms.MultipleChoiceField(choices=options, label='處理人', widget=forms.SelectMultiple(attrs={'class':'form-control'}), required=True) #要再改
    mensent = forms.ModelChoiceField(Category.objects.filter(categoryname__startswith="保"), label='處理人', widget=forms.Select(attrs={'class':'form-control'}), required=True) #要再改
    contractType = forms.ModelChoiceField(ContractType.objects.all(), label='合約型態', widget=forms.Select(attrs={'class': 'form-control'}), initial="W")
    # machineName = forms.ModelChoiceField(Machine.objects.select_related('hospitalid__areaid').filter(hospitalid__areaid=1).distinct(), label='機器名稱', widget=forms.Select(attrs={'class': 'form-control', 'id':'machinename'}), initial="TOMO")
    machineName = forms.ModelChoiceField(MachineName.objects.all(), label='機器分類', widget=forms.Select(attrs={'class': 'form-control', 'id':'machinename'}))
    machineid = MachineModelChoiceField(queryset=Machine.objects.select_related('hospitalid__areaid').filter(hospitalid__areaid=1), label='機器型號', widget=forms.Select(attrs={'class': 'form-control'}))
    callcont = forms.CharField(widget=forms.Textarea, label='叫修內容')
    brokenitems= forms.CharField(label='故障項目', widget=forms.TextInput(attrs={'class':'form-control'}))
    facid = forms.ModelChoiceField(Factory.objects.all(), label='更換零件(工廠碼)', widget=forms.Select(attrs={'class': 'form-control'}), initial="T011") #不入資料庫
    partsgpname = PartsgpnameModelChoiceField(queryset=Parts.objects.all(), label='(物料)', widget=forms.Select(attrs={'class': 'form-control'})) #不入資料庫
    partsid = PartsidModelChoiceField(queryset=Parts.objects.all(), label='', widget=forms.Select(attrs={'class': 'form-control','id':'partsid', 'name': 'partsid'})) #不入資料庫
    parts = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'partsall', 'type':'text'})) #入資料庫 零件號
    calltime = forms.TimeField(label='叫修時間', widget=forms.TimeInput(attrs={'class':'form-control', 'type': 'time'}))
    arrtime = forms.TimeField(label='到達時間', widget=forms.TimeInput(attrs={'class':'form-control', 'type': 'time'}))
    fixtime = forms.TimeField(label='維修時間', widget=forms.TimeInput(attrs={'class':'form-control', 'type': 'time', 'name':'input-time', 'id':'start-time'}))
    repairedtime = forms.TimeField(label='修復完成時間', widget=forms.TimeInput(attrs={'class':'form-control', 'type': 'time', 'id':'end-time'}))
    repairdur = forms.DurationField(label='維修時數', widget=forms.TextInput(attrs={'class':'form-control', 'id':'total-hours'})) #auto-count
    machinestpdur = forms.FloatField(label='停機時數', widget=forms.TextInput(attrs={'class':'form-control'}),)
    repaircont = forms.CharField(label='檢修內容', widget=forms.TextInput(attrs={'class':'form-control'}))
    note = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','cols': 80, 'rows': 1}), label='備註')


    class Meta:
        model = ServiceSheet  #models.py
        fields = '__all__'
        # fields = (' sheetid','empid', 'areaid', 'categoryid', 'stateid', 'date', 'machineStop', 'hospitalid', 'receiver', 'mensent', 'contractid', 'machinename', 'machineid', 'callcont', 'brokenitems', 'partsid', 'calltime', 'arrivetime', 'fixingtime', 'repairtime', 'repairdur', 'machinestpdur', 'repaircont', 'note', ) # 資料表的欄位名稱