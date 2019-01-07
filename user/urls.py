
from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
   path('index/',views.index.as_view(),name="index"),
   path('',views.user.as_view(),name='user'),
   path('search/',views.search.as_view(),name='search'),
   path('about/',views.about.as_view(),name='about'),
   path('othersfeed/',views.othersfeed.as_view(),name='othersfeed'),
   ]
