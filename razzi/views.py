from django.shortcuts import render_to_response
from django.template import RequestContext, Template
from django.views.generic import TemplateView


def home(request):
    context = {}
    return render_to_response("index.html", RequestContext(request, context))


class ResumeView(TemplateView):
    template_name = "resume.html"


class Blog(TemplateView):
    template_name = "iowa_js.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["posts"] = ["iowa_js.html"]
        return context


class Projects(TemplateView):
    template_name = "projects.html"
