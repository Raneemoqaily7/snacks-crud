from django.urls import path 

from .views import HomeView , SnackCreatView


urlpatterns = [
    path("" , HomeView.as_view() , name ="home"),
    path("create/" ,SnackCreatView.as_view() , name ="create"),

]


