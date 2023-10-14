from . import views
from django.urls import path


urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("list", views.ProfilesView.as_view())
] 
