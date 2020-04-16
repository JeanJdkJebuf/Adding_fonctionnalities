from django.urls import path, re_path

from . import views

urlpatterns = [
    path("research_substitute/", views.research_substitute, name="research_substitute"),
    path("details/<int:product_id>/", views.detail, name="detail"),
    path("details/<int:product_id>/<int:previousprod_id>/", views.detail, name="detail"),
    path("ajax_search/", views.autocomplete, name="autocomplete"),
]
