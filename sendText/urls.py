from django.urls import path
from .import views

app_name = 'sendText'


urlpatterns = [
    path('', views.index, name='index'),
    path('send_email/', views.send_email, name='send_email'),
    path('success', views.success, name='success'),
    path('send_sms/', views.send_sms, name='send_sms'),
    path('sms_success', views.sms_success, name='sms_success'),
    path('select/', views.select, name='select'),
    
]
