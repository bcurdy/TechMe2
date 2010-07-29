from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'podcast.episodes.views.main_page'),
    (r'^more/(?P<offset>\d+)/$', 'podcast.episodes.views.more_episodes'),
    (r'^rss2$', 'podcast.episodes.feeds.rss'),
    (r'^about/$', 'podcast.episodes.views.about'),
    (r'^contact/$', 'podcast.episodes.views.contact'),
    (r'^search/$', 'podcast.episodes.views.search'),
    (r'^startups/interviews/map/$','podcast.episodes.views.map'),
    (r'^startups/interviews.kml$','podcast.episodes.feeds.kml'),
    (r'^startups/(?P<slug>[a-zA-Z0-9_-]+)/$','podcast.episodes.views.single'),
    (r'^admin/add/$','podcast.episodes.views.add'),
    (r'^admin/edit/(?P<slug>[a-zA-Z0-9_-]+)/$','podcast.episodes.views.edit'),
    # Example:
    # (r'^podcast/', include('podcast.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
