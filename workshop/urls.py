from django.conf.urls import url
from .views import WorkShopListView, WorkshopDetailView, WorkshopCreateView, WorkshopUpdateView, WorkshopDeleteView


urlpatterns = [
    url(r'^$', WorkShopListView.as_view(), name='list'),
    url(r'^create/$', WorkshopCreateView.as_view(), name='create'),
    url(r'^detail/(?P<pk>\d+)/$', WorkshopDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', WorkshopUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', WorkshopDeleteView.as_view(), name='delete'),
]
