from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^$', 'podcast.episodes.views.main_page'),
    (r'^about/$', direct_to_template, {'template': 'about.html'}),
    (r'^contact/$', direct_to_template, {'template': 'contact.html'}),
    (r'interview_process', direct_to_template, {'template': 'interview_process.html'}),  
    (r'^more/(?P<offset>\d+)/$', 'podcast.episodes.views.more_episodes'),
    (r'^rss2$', 'podcast.episodes.feeds.rss'),
    (r'^search/$', 'podcast.episodes.views.search'),
    (r'^startups/interviews/map/$','podcast.episodes.views.map'),
    (r'^startups/interviews.kml$','podcast.episodes.feeds.kml'),
    (r'^startups/(?P<slug>[a-zA-Z0-9_-]+)/$','podcast.episodes.views.single'),
    #admin section
    (r'^admin/add/$','podcast.episodes.views.add'),
    (r'^admin/edit/(?P<slug>[a-zA-Z0-9_-]+)/$','podcast.episodes.views.edit'),
)
