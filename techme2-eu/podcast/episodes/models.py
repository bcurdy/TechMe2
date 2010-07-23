from google.appengine.ext.webapp import template
from google.appengine.ext import db

from google.appengine.ext.db import djangoforms

class Episode(db.Model):
  #Title
  title = db.StringProperty(required=True)
  slug = db.StringProperty(required=True)
  #Meta
  interviewee = db.StringProperty(required=True)
  organization = db.StringProperty(required=True)
  country = db.CategoryProperty(required=True)
  city = db.CategoryProperty(required=True)
  coordinates = db.GeoPtProperty(required=True)
  tags = db.StringListProperty(required=True)
  #Content
  short_description = db.StringProperty(required=True)
  interview_notes = db.TextProperty(required=True)
  published_on = db.DateProperty(auto_now_add=True)
  published_by = db.UserProperty()
  is_draft = db.BooleanProperty(default=True)
  thumbnail = db.LinkProperty()
  #Finally the show :)
  mp3 = db.LinkProperty(required=True)
  byte_length = db.IntegerProperty(required=True)
  
  def __unicode__(self):
        return self.slug
  
class AddEpisode(djangoforms.ModelForm):
  def __init__ (self, *args, **kwargs): 
    super(AddEpisode, self).__init__(*args, **kwargs) 
    self.fields['tags'].widget.attrs['rows'] = '1'
    self.fields['interview_notes'].widget.attrs['rows'] = '10'
    self.fields['interview_notes'].widget.attrs['cols'] = '100'

  class Meta:
    model = Episode
    exclude = ['published']

