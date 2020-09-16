from django.urls import path

from . import views


app_name='Contact'


urlpatterns = [
    path('',views.send_massage, name ='Contact'),
]