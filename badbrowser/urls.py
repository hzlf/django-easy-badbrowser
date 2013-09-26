# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from .views import ignore, unsupported

urlpatterns = patterns("",
    url(r"^$", unsupported, name="django-badbrowser-unsupported"),
    url(r"^ignore/$", ignore, name="django-badbrowser-ignore"),
)
