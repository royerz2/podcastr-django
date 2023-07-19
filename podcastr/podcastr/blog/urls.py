from django.conf.urls import include, url

from podcastr.blog import views

urlpatterns = [
    url(
        r'^$',
        views.EntryListView.as_view(),
        name='entries'
    ),
    url(
        r'^(?P<slug>[-\w]+)/$',
        views.EntryView.as_view(),
        name='entry'
    ),
]
