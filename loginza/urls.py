from django.conf.urls.defaults import *


urlpatterns = patterns(
    'loginza.views',
    url(r'^$', 'loginza_callback', name='loginza'),
)
