from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$',                                         'bookmarks.views.index'),

    # link list object routing
    url(r'^linklist/create/$',                         'bookmarks.views.createlinklist'),
    url(r'^linklist/createpost/$',                     'bookmarks.views.createlinklistpost'),
    url(r'^linklist/retrieve/(?P<linklist_id>\d+)/?$', 'bookmarks.views.retrievelinklist'),
    url(r'^linklist/update/(?P<linklist_id>\d+)$',     'bookmarks.views.updatelinklist'),   
    url(r'^linklist/delete/(?P<linklist_id>\d+)$',     'bookmarks.views.deletelinklist'),
    url(r'^linklist/listall/$',                        'bookmarks.views.listalllinklist'),
    url(r'^linklist/addlink/(?P<linklist_id>\d+)$',    'bookmarks.views.linklistcreateaddlink'),
    url(r'^linklist/addlinkpost/$',                    'bookmarks.views.linklistcreateaddlinkpost'),

    # link object routing
    url(r'^link/create/$',                             'bookmarks.views.createlink'),
    url(r'^link/retrieve/(?P<link_id>\d+)$',           'bookmarks.views.retrievelink'),
    url(r'^link/update/(?P<link_id>\d+)$',             'bookmarks.views.updatelink'),
    url(r'^link/delete/(?P<link_id>\d+)$',             'bookmarks.views.deletelink'),
    url(r'^link/listall/$',                            'bookmarks.views.listalllink'),


    # admin interface routing
    url(r'^admin/?', include(admin.site.urls)),

)
