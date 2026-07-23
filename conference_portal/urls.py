from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.template.loader import render_to_string

from django.conf import settings
from django.conf.urls.static import static


def robots_txt(request):
    domain = request.build_absolute_uri("/")
    return HttpResponse(
        f"User-agent: *\nAllow: /\nDisallow: /dashboard/\nDisallow: /broadcast/\nDisallow: /admin/\n\nSitemap: {domain}sitemap.xml\n",
        content_type="text/plain",
    )


def sitemap_xml(request):
    # Public, search-engine-relevant pages only. Add new page names here
    # whenever you add a new public URL you want Google to index.
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

# NOTE: Django serving media files itself is not the most efficient way to
# do it at large scale, but for a conference site's traffic level it is
# perfectly fine and much simpler than configuring a separate storage
# service. This used to only run when DEBUG=True, which meant uploaded
# papers/photos/receipts would 404 in production - now it works in both.
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)