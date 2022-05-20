from django.shortcuts import render
from django.views.generic import (
                            TemplateView,
                            ListView,
                            DeleteView,
                            DetailView,
                            CreateView,
                            UpdateView
                        )

from .models import Snack
# Create your views here.

class HomeView (TemplateView):
    template_name = "home.html"

class SnackCreatView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields=["title" , "description"]





