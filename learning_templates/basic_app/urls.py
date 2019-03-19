from django.conf.urls import url
from basic_app import views
from django.urls import path

#TEMPLE TAG
app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
    path('',views.other,name='index'),
]
