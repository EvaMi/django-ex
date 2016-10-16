from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health, detail, results, vote, detail 

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<question_id>[0-9]+)/$', detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),
    url(r'^specifics/(?P<question_id>[0-9]+)/$', detail, name='detail'),
]
