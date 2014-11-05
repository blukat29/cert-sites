from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from forms import RegistrationForm

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cert.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^report/', include('report.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^register/', CreateView.as_view(template_name="register.html",
                                          form_class=RegistrationForm,
                                          success_url="/")),
)
