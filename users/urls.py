from django.urls import path

from . import views

urlpatterns = [
    # Create user
    path("create_user/", views.create_user, name="create_user"),
    # log user
    path("log_in/", views.log_in, name="log_in"),
    # disconnect
    path("disconnect_user/", views.disconnect_user, name="disconnect_user"),
    # user_informations
    path("user_informations/", views.user_informations, name="user_informations"),
    # edit_user
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    # modify password
    path("edit_profile/change_password/", views.change_password, name="change_password"),

]
