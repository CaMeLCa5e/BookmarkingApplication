from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookmarks.views import IndexPage, CreateListView, ListDetailView, CreateLinkView, LinkDetailView


urlpatterns = patterns('',
    # admin
    url(r'^admin/', include(admin.site.urls)),

    # bookmarker
    url(r'^$', IndexPage.as_view(), name='index'),

    url(r'^bookmarks/new/$', 
        CreateListView.as_view(),
        name='list-new'),

    url(r'^bookmarks/list/(?P<pk>[0-9]+)/$', 
        ListDetailView.as_view(), 
        name='list-detail'),

    url(r'^bookmarks/link/new/$', 
        CreateLinkView.as_view(),
        name='link-new'),

    url(r'^bookmarks/link/(?P<pk>[0-9]+)/$',
        LinkDetailView.as_view(),
        name='link-detail'),

)
