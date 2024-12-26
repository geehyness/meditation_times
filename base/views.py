from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Message
#from.models import Task


# Create your views here.
class MTList(ListView):
    model = Message
    context_object_name = 'messages'
    template_name = 'base/home.html'

class Message(DetailView):
    model = Message
    context_object_name = 'message'
    template_name = "base/message.html"
