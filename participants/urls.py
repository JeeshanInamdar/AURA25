from django.urls import path
from participants import views

urlpatterns = [
    path('',views.home,name='home'),
    path('form/',views.form,name='form'),
    path('submit/',views.submit_form,name='submit_form')
]