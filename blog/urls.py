from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('ui_buttons',views.ui_buttons, name='ui_buttons'),
    path('test',views.test, name='test'),
    path('boxplot',views.boxplot, name='boxplot'),
    path('barchart',views.barchart, name='barchart'),
    path('simple_upload',views.simple_upload, name='simple_upload'),
]