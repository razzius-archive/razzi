from django.conf.urls import patterns
from django.conf import settings

from razzi.views import home, ResumeView, Blog, Projects

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    (r"^$", home),
    (r"^resume/$", ResumeView.as_view()),
    (r"^blog/$", Blog.as_view()),
    (r"^blog/(.*)/$", Blog.as_view()),
    (r"^projects/$", Projects.as_view()),
    (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
