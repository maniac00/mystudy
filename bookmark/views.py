from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Create your views here.

#- - - List View
class BookmarkLV(ListView):
    model = Bookmark

#- - - DetailView
class BookmarkDV(DetailView):
    model = Bookmark