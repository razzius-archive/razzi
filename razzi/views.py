from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "index.html"


class Resume(TemplateView):
    template_name = "resume.html"


class Blog(TemplateView):
    template_name = "blog.html"


class Projects(TemplateView):
    template_name = "projects.html"
