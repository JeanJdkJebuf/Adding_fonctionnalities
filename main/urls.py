from django.urls import path

from . import views

urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('copyright/', views.copyright, name="copyright"),
]
