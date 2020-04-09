from django.urls import path

from . import views

urlpatterns = [
    path("add_favorites/", views.add_favorites, name="add_favorites"),
    path("favorites/", views.consult_favorites, name="consult_favorites"),
    path(
        "favorites/?page=<int:page>",
        views.consult_favorites,
        name="consult_favorites",
    ),
]
