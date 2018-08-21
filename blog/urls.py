from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('ui_buttons',views.ui_buttons, name='ui_buttons'),
    path('test',views.test, name='test'),
]