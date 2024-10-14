from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('host/',views.host,name='host'),
    path('participant/',views.participant,name='participant'),
    path('host/validate/',views.qr_validation,name='qr_validation'),
    path('host/check_qr_code/',views.check_qr_code,name='check_qr_code'),
    path('form/',views.form,name='form'),
    path('submit/',views.submit_form,name='submit_form'),
    path('host/scan/',views.scan,name='scan'),
    path('qr_code_scan/', views.qr_code_scan, name='qr_code_scan'),
]