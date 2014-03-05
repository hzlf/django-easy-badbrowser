# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import ignore, UnsupportedBrowser

urlpatterns = patterns("",
    #url(r"^$", UnsupportedBrowser.as_view(), name="django-badbrowser-unsupported"),
    url(r"^ignore/$", ignore, name="django-badbrowser-ignore"),
)
