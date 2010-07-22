from django.shortcuts import render_to_response

def rss(request):
  data_dictionary = {}
  return render_to_response("base_rss.xml", data_dictionary) 