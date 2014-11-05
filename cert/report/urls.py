from django.conf.urls import patterns, include, url

from report import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="report_index"),
)
