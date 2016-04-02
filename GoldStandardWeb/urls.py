from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^generator/', include('generator.urls')),
    url(r'^admin/', admin.site.urls),
]

