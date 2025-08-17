from music import views
from django.urls import path

urlpatterns=[
    path('',views.get_genres)
]