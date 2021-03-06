from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from core import views
from messaging.views import twilio

urlpatterns = patterns('',
    url(r'^m/incident', views.mobile_incident),
    url(r'^m/incidentvote', views.mobile_incident_vote),
    url(r'^m/register', views.mobile_register),
    url(r'^m/listincidents', views.mobile_listincidents),
    url(r'^m/listusers', views.mobile_listusers),
    url(r'^m/notifybeat', views.mobile_notifybeat),
    url(r'^m/login', views.mobile_login),
    url(r'^m/logout', views.mobile_logout),
    url(r'm/report', views.mobile_report),
    url(r'^m', views.mobile_index),
    url(r'^smshook', twilio),
    url(r'^admin', include(admin.site.urls)),
    url(r'', views.mobile_index,name="registersubmit")
)


