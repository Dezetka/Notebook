from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/welcome.html'

class AuthorizedViews(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'


