from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index_blog),
    path('whoami/', views.whoami),
    path('portifolio/', views.portifolio)
]
