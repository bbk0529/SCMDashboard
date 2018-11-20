from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import scm_views
from django.conf import settings
from django.conf.urls.static import static
# import scm_views

urlpatterns=[
    path('',scm_views.listAssay, name='listAssay'),
    path('approvalPlan', scm_views.approvalPlan, name='approvalPlan'),
    path('changeLog',scm_views.changeLog, name='changeLog'),
    path('setting',scm_views.setting, name='setting'),
    path('approvalPlanQuery', scm_views.approvalPlanQuery, name='approvalPlanQuery'),
    path('approvalPlanCreate', scm_views.approvalPlanCreate, name='approvalPlanCreate'),
    path('assayQuery',scm_views.assayQuery, name='assayQuery'),
    path('updateQuery',scm_views.updateQuery, name='updateQuery'),
    url(r'^export/xls/data/$', scm_views.export_data_xls, name='export_data_xls'),
    url(r'^export/xls/log/$', scm_views.export_log_xls, name='export_log_xls'),
    url('import_data_xls', scm_views.import_data_xls, name='import_data_xls'),
    # url(r'^uploads/simple/$', scm_views.upload, name='upload'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
