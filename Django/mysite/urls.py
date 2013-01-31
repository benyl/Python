from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^polls/', include('polls.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # django-registration
    url(r'^accounts/', include('registration.backends.default.urls')),
)

urlpatterns += patterns('mysite.views',
    url(r'^hello/$','hello'),
    url(r'^dbForm1/$','dbForm1'),
    url(r'^dbForm2/$','dbForm2'),
    url(r'^dbForm3/$','dbForm3'),
)
