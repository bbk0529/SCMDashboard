from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import scm_views

urlpatterns=[
    path('list',scm_views.listAssay, name='listAssay'),
    path('', scm_views.approvalPlan, name='approvalPlan'),
    path('approvalPlanQuery', scm_views.approvalPlanQuery, name='approvalPlanQuery'),
    path('approvalPlanCreate', scm_views.approvalPlanCreate, name='approvalPlanCreate'),
    path('assayQuery',scm_views.assayQuery, name='assayQuery'),
    path('updateQuery',scm_views.updateQuery, name='updateQuery'),
    path('changeLog',scm_views.changeLog, name='changeLog'),    
]
