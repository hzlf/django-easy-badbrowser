# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template


def unsupported(request):

    if hasattr(settings, "BADBROWSER_SUGGEST"):
        suggest = settings.BADBROWSER_SUGGEST
    else:
        suggest = ("firefox",)

    if hasattr(settings, "BADBROWSER_BASE_TEMPLATE"):
        base_template = settings.BADBROWSER_BASE_TEMPLATE
    else:
        base_template = "badbrowser/base.html"

    return direct_to_template(request, "badbrowser/unsupported.html", {
            "next": request.path,
            "suggest": suggest,
            "base_template": base_template
            })


def ignore(request):
    response = HttpResponseRedirect(request.GET["next"] if "next" in request.GET else "/")
    response.set_cookie("badbrowser_ignore", True)
    return response
