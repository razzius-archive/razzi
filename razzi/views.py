from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView


def home(request):
    context = {}
    return render_to_response("index.html", RequestContext(request, context))


class ResumeView(TemplateView):
    template_name = "resume.html"
