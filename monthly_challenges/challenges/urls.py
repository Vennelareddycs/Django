from django.urls import path
from .import views

urlpatterns=[
    path("",views.index, name="index"),
    path("january", views.january),
    path("february", views.february),
    #path("<month>", views.monthly_challenge_month),
    path("<int:day>", views.weekly_challenge_by_number),
    path("<str:day>", views.weekly_challenge, name="week")
 
]

