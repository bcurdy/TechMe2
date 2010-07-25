import datetime
from podcast.episodes.models import AddEpisode
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from google.appengine.ext import db


def main_page(request):
  count_query = db.GqlQuery("SELECT __key__ FROM Episode WHERE is_draft = False")
  count_episodes = count_query.count()
  
  display = 5
  if count_episodes < display+1:
    pages = []
  else:
    pages = range(1,(count_episodes/display)+2)
  
  display_query = db.GqlQuery("SELECT * FROM Episode ORDER BY published_on DESC")
  episodes = display_query.fetch(display,0)
  post_title = "Last shows"
 
  data_dictionary = {'page_title': 'European Startups',
                     'post_title': post_title,
                     'episodes': episodes,
                     'pages': pages,
                    }
  return render_to_response('main.html', data_dictionary)

def more_episodes(request, offset):
  limit = 5
  starts = (int(offset)-1)*limit
  display_query = db.GqlQuery("SELECT * FROM Episode ORDER BY published_on DESC")
  episodes = display_query.fetch(limit, starts)
  data_dictionary = {'episodes': episodes}
  return render_to_response('more.html', data_dictionary)

def about(request):
  return render_to_response("about.html", {})
  
def contact(request):
  return render_to_response("contact.html", {})
  
def add(request): 
  if request.method == 'POST':
    form = AddEpisode(request.POST)
    if form.is_valid():
      new_episode = form.save(commit=False)
      new_episode.put()
      return HttpResponseRedirect('/')
  else:
    form = AddEpisode()
  data_dictionary = {'form': form,
                     'action': 'add'}
  return render_to_response("add_episode.html", data_dictionary)
    
def edit(request, slug):
   query = db.GqlQuery("SELECT * FROM Episode WHERE slug = :1 ", slug)
   episode = query.get()
   if request.method == 'POST':
     form = AddEpisode(request.POST, instance = episode)
     if form.is_valid():
       edited_episode = form.save(commit=False)
       edited_episode.put()
       return HttpResponseRedirect('/')
   else:
     form = AddEpisode(instance = episode)
     data_dictionary = {'form': form,
                        'action': 'edit',
                        'slug': slug}
     return render_to_response("add_episode.html", data_dictionary)
 

def map(request):
  current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-00")
  return render_to_response('map.html', {'refresh_time': current_time})
  
def single(request, slug):
  query = db.GqlQuery("SELECT * FROM Episode WHERE slug = :1 ", slug)
  episode = query.get()
  if not episode:
    raise Http404
  data_dictionary = {'episode': episode}
  return render_to_response('episode.html', data_dictionary)