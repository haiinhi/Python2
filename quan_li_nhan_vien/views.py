from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import UpdateNhanvienNameForm
from .forms import DeleteNhanvienForm
# Create your views here.
def views_nhanvien(request):
    Nhan_viens = Nhan_vien.objects.all()
    return HttpResponse(Nhan_viens)

def update_nhanvien_name_using_form(request):
    if request.method == 'POST':
        form = UpdateNhanvienNameForm(request.POST)
        if form.is_valid():
            cccd = form.cleaned_data['cccd']
            new_ten_nhanvien = form.cleaned_data['ten_nhanvien']
            Nhan_vien.objects.filter(cccd=cccd).update(ten_nhanvien=new_ten_nhanvien)
            return HttpResponse('Cap nhat ten nhan vien thanh cong!')
    
    form = UpdateNhanvienNameForm()
    return render(request, 'nhan_vien.html', {'form': form})

def delete_nhanvien_name_using_form(request):
    if request.method == 'POST':
        form = DeleteNhanvienForm(request.POST)
        if form.is_valid():
            cccd = form.cleaned_data['cccd']
            Nhan_vien.objects.filter(cccd=cccd).delete()
            return HttpResponse('Xoa nhan vien thanh cong!')
        else:
            return HttpResponse(form.errors.as_text())
  
    form = DeleteNhanvienForm()
    return render(request, 'nhan_vien.html', {'form': form})