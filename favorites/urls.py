from django.urls import path

from . import views

urlpatterns = [
    path("add_favorites/", views.add_favorites, name="add_favorites"),
    path("consult_favorites/", views.consult_favorites, name="consult_favorites"),
    path("consult_favorites/?page=<int:page>/", views.consult_favorites, name="consult_favorites"),
]
