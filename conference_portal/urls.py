from django.contrib import admin
from django.urls import path, re_path, include
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.static import serve as serve_static

from django.conf import settings
from django.conf.urls.static import static


def robots_txt(request):
    domain = request.build_absolute_uri("/")
    return HttpResponse(
        f"User-agent: *\nAllow: /\nDisallow: /dashboard/\nDisallow: /broadcast/\nDisallow: /admin/\n\nSitemap: {domain}sitemap.xml\n",
        content_type="text/plain",
    )


def sitemap_xml(request):
    page_names = [
        "home", "register", "submit_paper", "contact",
    ]
    urls = []
    from django.urls import reverse
    for name in page_names:
        try:
            urls.append(request.build_absolute_uri(reverse(name)))
        except Exception:
            pass
    xml = render_to_string("sitemap.xml", {"urls": urls})
    return HttpResponse(xml, content_type="application/xml")


urlpatterns = [

    path("robots.txt", robots_txt, name="robots_txt"),
    path("sitemap.xml", sitemap_xml, name="sitemap_xml"),

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('conference.urls')
    ),

]

urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve_static,
        {"document_root": settings.MEDIA_ROOT},
    ),
]