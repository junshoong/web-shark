from django.conf.urls import patterns, include, url
from django.contrib import admin
import capture.views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', capture.views.home_page),
    # url(r'^capture/', include('capture.urls')),
]
