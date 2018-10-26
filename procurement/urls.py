from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import scm_views

urlpatterns=[
    path('',scm_views.main, name='scm'),
    path('assayQuery',scm_views.assayQuery, name='assayQuery'),
    path('updateQuery',scm_views.updateQuery, name='updateQuery'),
    path('deleteQuery',scm_views.deleteQuery, name='deleteQuery'),
]
