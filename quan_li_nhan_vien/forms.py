from django import forms
from.models import *

class UpdateNhanvienNameForm(forms.Form):
    cccd = forms.CharField(label='So')
    ten_nhanvien = forms.CharField(label='Ten nhan vien')
    
#class UpdateDocgiaNameForm(forms.ModelForm):
#    class Meta:
#        model = Docgia
#        fields = ['ma_dg', 'ten_dg']
#        labels = {
#            'ma_dg': 'Ma doc gia',
#            'ten_dg': 'Ten doc gia moi',
#        } 

class DeleteNhanvienForm(forms.Form):
    cccd = forms.CharField(label='So can cuoc')