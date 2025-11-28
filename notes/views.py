from django.shortcuts import render
from .models import Notes
from django.views.generic import ListView,  DetailView

# Create your views here.

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "layout/templates/notes/notes_list.html" 

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
