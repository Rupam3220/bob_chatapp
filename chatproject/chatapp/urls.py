from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('specific_func', views.specific_func, name='specific_func'),
    
    path('getResponse', views.getResponse, name='getResponse'),
]