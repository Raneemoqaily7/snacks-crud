from django.shortcuts import render
from django.views.generic import (
                            TemplateView,
                            ListView,
                            DeleteView,
                            DetailView,
                            CreateView,
                            UpdateView
                        )

# Create your views here.

class HomeView (TemplateView):
    template_name = "home.html"



