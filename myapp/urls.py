from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home  , name='index'),
    url(r'^packages$', views.packages  , name='packages'),
    url(r'^package/(?P<id>\d+)$', views.packagedetail  , name='packagedetail'),
    url(r'^packagedetailed$', views.packagedetailed  , name='packagedetailed'),
    url(r'^service/(?P<id>\d+)$', views.servicedetail  , name='servicedetail'),
    url(r'^servicedetailed$', views.servicedetailed  , name='servicedetailed'),
    url(r'^services$', views.services  , name='services'),
    url(r'^products$', views.products  , name='products'),
    url(r'^product/(?P<id>\d+)$', views.productdetail  , name='productdetail'),
    url(r'^productdetailed$', views.productdetailed  , name='productdetailed'),
    url(r'^about$', views.about  , name='about'),
    url(r'^contact$', views.contact  , name='contact'),
    url(r'^contacted$', views.contacted  , name='contacted'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)