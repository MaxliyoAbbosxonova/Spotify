from music import views
from django.urls import path

urlpatterns=[
    path('',views.genre_list_or_create)
]