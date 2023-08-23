from django.contrib import admin
from django.urls import path
from. import views
urlpatterns = [
    path('',views.landingurl,name='landingurl'),
    path('filesubmit',views.filesub,name="filesubmit"),
]
