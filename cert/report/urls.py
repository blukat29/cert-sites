from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from report import views
from report.views import ReportCreateView, ReportUpdateView

urlpatterns = patterns('',
    url(r'^$', views.index, name="report_index"),
    url(r'^create/$', login_required(ReportCreateView.as_view()), name="report_create"),
    url(r'read/(?P<report_id>\d+)/$', views.read, name="report_read"),
    url(r'edit/(?P<report_id>\d+)/$', login_required(ReportUpdateView.as_view()), name="report_update"),
)
