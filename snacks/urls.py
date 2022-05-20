from django.urls import path 

from .views import HomeView , SnackCreatView , SnackDetailView ,SnackUpdateView ,SnackDeleteView


urlpatterns = [
    path("" , HomeView.as_view() , name ="home"),
    path("create/" ,SnackCreatView.as_view() , name ="create"),
    path("<int:pk>/" ,SnackDetailView.as_view() , name ="detail"),
    path("update/<int:pk>" ,SnackUpdateView.as_view() , name ="update"),
    path("delete/<int:pk>" ,SnackDeleteView.as_view() , name ="delete")



]


