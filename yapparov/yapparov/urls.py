
from form import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path("appointment/", views.appointment),
    path("dost/", views.dost),
]
