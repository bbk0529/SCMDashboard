#URL LO Team
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns=[
    # path('',views.tab1, name='tab1'),
    #path('', TemplateView.as_view(template_name='./blog/index.html'), name='index'),
    path('tab3',views.tab3, name='tab3'),
    path('tab2',views.tab2, name='tab2'),
    path('consumption',views.index, name='consumption'),
    path('ui_buttons',views.ui_buttons, name='ui_buttons'),
    path('boxplot',views.boxplot, name='boxplot'),
    path('barchart',views.barchart, name='barchart'),
    path('barchart2',views.barchart2, name='barchart2'),
    path('get_name',views.get_name, name='get_name'),
    path('productFamily',views.productFamily, name='productFamily'),
    path('simple',views.simple, name='simple'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
