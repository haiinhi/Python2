from django.urls import path
from .import views

urlpatterns = [
    path('views_nhanvien', views.views_nhanvien, name='views_nhanvien'),
    path('update_nhanvien_name_using_form', views.update_nhanvien_name_using_form, name='update_nhanvien_name_using_form'),
    path('delete_nhanvien_name_using_form', views.delete_nhanvien_name_using_form, name='delete_nhanvien_name_using_form'),
]
