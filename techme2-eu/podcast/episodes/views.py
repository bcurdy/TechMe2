from podcast.episodes.models import AddEpisode
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from google.appengine.ext import db


def main_page(request):
  query = db.GqlQuery("SELECT * FROM Episode ORDER BY published_on DESC")
  episodes = query.fetch(10)
  post_title = "Last shows"
 
  data_dictionary = {'page_title': 'European Startups',
                     'post_title': post_title,
                     'episodes': episodes,
                    }
  return render_to_response('main.html', data_dictionary)
    
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
  
def single(request, slug):
  query = db.GqlQuery("SELECT * FROM Episode WHERE slug = :1 ", slug)
  episode = query.get()
  data_dictionary = {'episode': episode}
  return render_to_response('episode.html', data_dictionary)