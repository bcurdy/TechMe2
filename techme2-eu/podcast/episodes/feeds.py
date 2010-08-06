import datetime
from podcast.episodes.models import Episode
from podcast.episodes.models import AddEpisode
from django.contrib.gis.shortcuts import render_to_kml 
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from google.appengine.ext import db

def rss(request):
  query = db.GqlQuery("SELECT * FROM Episode ORDER BY published_on DESC")
  episodes = query.fetch(10)
  last_published_on = episodes[0].published_on
  data_dictionary = {'episodes': episodes,
                     'last_published_on': last_published_on,}
  return render_to_response("base_rss.xml", data_dictionary, mimetype='application/xml') 
  
def kml(request):
  episodes = Episode.all()
  return render_to_kml('interviews.kml', {'episodes':episodes})
