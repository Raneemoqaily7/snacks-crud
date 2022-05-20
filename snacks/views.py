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
    fields=["title" ,"purchaser", "description"]

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack

class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields=["title" , "description"]

class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url= '/'







