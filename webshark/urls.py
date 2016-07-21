from django.conf.urls import patterns, include, url
from django.contrib import admin
from capture import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page),
    url(r'^capture/', views.capture),
    # url(r'^capture/', include('capture.urls')),
]
