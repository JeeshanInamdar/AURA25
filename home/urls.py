from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('host/',views.host,name='host'),
    path('participant/',views.participant,name='participant'),
    path('form/',views.form,name='form'),
    path('host/scan/',views.scan,name='scan'),
    path('qr_code_scan/', views.qr_code_scan, name='qr_code_scan'),
]