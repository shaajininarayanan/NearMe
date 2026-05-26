from django.urls import path
from . import views

urlpatterns = [
    path("", views.map_page, name="map"),
    path("beach/", views.beach, name="beach"),
    path("fort/", views.fort, name="fort"),
    path("college/", views.college, name="college"),
]