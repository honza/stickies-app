from django.conf.urls.defaults import *
import os
from settings import PROJECT_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^stickies/', include('stickies.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'notes.views.index'),
    (r'^project/(?P<id>[0-9]+)/$', 'notes.views.project'),
    (r'^ajax/', 'notes.views.ajax'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(PROJECT_ROOT, 'media')}),
    
    (r'accounts/login/$', 'django.contrib.auth.views.login'),
    (r'accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}),
)


