from django.conf.urls.defaults import include, patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'),
        name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^loginza/', include('loginza.urls')),
)
