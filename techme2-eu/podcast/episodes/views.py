import datetime
from podcast.episodes.models import AddEpisode
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from google.appengine.ext import db


def main_page(request):
  """Main page displaying 'shows_to_display' last shows"""
   
  shows_to_display = 5
  
  # Counts shows and set how many pages are needed to display them based on shows by page ('shows_to_display' variable)
  count_query = db.GqlQuery("SELECT __key__ FROM Episode WHERE is_draft = False")
  count_episodes = count_query.count()
  if count_episodes < shows_to_display+1:
    pages = []
  elif count_episodes%shows_to_display == 0:
    pages = range(1,(count_episodes/shows_to_display)+1)
  else: 
    pages = range(1,(count_episodes/shows_to_display)+2)
  
  #Retrieve the first 'shows_to_display' shows to show on main page
  display_query = db.GqlQuery("SELECT * FROM Episode ORDER BY published_on DESC")
  episodes = display_query.fetch(shows_to_display,0)
 
  data_dictionary = { 'episodes': episodes,
                                'pages': pages }
  return render_to_response('main.html', data_dictionary)

def more_episodes(request, offset):
  """Fetch 'limit' additional shows to display on main instead of last shows
  
  Args:
    offset: Page number (which page are we displaying)
  """
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
  
def map(request):
  """Display a map of all the shows recorded until now
  
     current_time is used to force Google maps to refresh iteself hourly
   """
  current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-00")
  return render_to_response('map.html', {'refresh_time': current_time})
 
def search(request):
  """Sends a query to Google custom search"""
  if request.POST:
    search_query = request.POST["q"]
  else:
    search_query = ''
  return render_to_response('search.html',{'search_query': search_query})
 
def single(request, slug):
  """Displays a single episode
  
  Args:
    slug: the slug of the episode to display (string, no space, no funky chars)
   """
  query = db.GqlQuery("SELECT * FROM Episode WHERE slug = :1 ", slug)
  episode = query.get()
  if not episode:
    raise Http404
  data_dictionary = {'episode': episode}
  return render_to_response('episode.html', data_dictionary)  
  
  
### Admin ###

def add(request): 
  """Adds a new show"""
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
   """Edits a show
   
   Args:
     slug: the slug of the episode to edit (string, no space, no funky chars)
   """
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