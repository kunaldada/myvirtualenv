"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from mysite.views import hello, current_datetime, hours_ahead, dummy_view
from . import views
from . import views as credit_views
from books.views import getObject

extra_patterns = [
    url(r'^reports/(?P<id>[0-9]{1})/$', credit_views.reports),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', views.hello),	
    url(r'^time/$', views.current_datetime),
    url(r'^dummyview/$', views.dummy_view),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^get_obj/$', getObject),
    url(r'^reviews/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    url(r'^reviews/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$',views.review_detail),
    url(r'^credit/', include(extra_patterns)),
]
