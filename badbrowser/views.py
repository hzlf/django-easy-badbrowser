# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse, SimpleTemplateResponse


class UnsupportedBrowser(SimpleTemplateResponse):

    template_name = 'my_template.html'

    def get(self, request, *args, **kwargs):
        print request
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

def unsupported(request):

    if hasattr(settings, "BADBROWSER_SUGGEST"):
        suggest = settings.BADBROWSER_SUGGEST
    else:
        suggest = ("firefox",)

    if hasattr(settings, "BADBROWSER_BASE_TEMPLATE"):
        base_template = settings.BADBROWSER_BASE_TEMPLATE
    else:
        base_template = "badbrowser/base.html"
    t = TemplateResponse(request, 'badbrowser/unsupported.html', {
            "next": request.path,
            "suggest": suggest,
            "base_template": base_template
            })
    return t.render()

def ignore(request):
    response = HttpResponseRedirect(request.GET["next"] if "next" in request.GET else "/")
    response.set_cookie("badbrowser_ignore", True)
    return response
