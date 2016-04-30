from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('generator/')),
    url(r'^polls/', include('polls.urls')),
    url(r'^generator/', include('generator.urls')),
    url(r'^admin/', admin.site.urls),
]

