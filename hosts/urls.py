from django.urls import path
from hosts import views

urlpatterns = [
    path('',views.home,name='home'),
    path('validate/',views.qr_validation,name='qr_validation'),
    path('check_qr_code/',views.check_qr_code,name='check_qr_code'),
]