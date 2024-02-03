from django.urls import path
from BookApp import views

urlpatterns = [
    path('addbook', views.addbook),               #Create
    path('home', views.homepage),                 #Read
    path('update/<bookid>', views.updatebook),    #Update
    path('delete/<bookid>', views.deletebook),    #Delete
]