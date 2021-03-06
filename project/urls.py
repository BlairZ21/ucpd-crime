from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from ucpd.views import Main, BinsJSON, BinDetailJSON, months, hours

urlpatterns = [
    url(r'^$', Main.as_view(), name='bins'),
    url(r'^api/bins.json$', BinsJSON.as_view(), name='bins-json'),
    url(r'^api/bin/(?P<pk>[-\w]+).json$', BinDetailJSON.as_view(),
    	name='bin-json'),

    # Generates CSVs, which must be moved into the static directory. Hacks!
    url(r'^months.csv$', months, name='months'),
    url(r'^hours.csv$', hours, name='hours'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
