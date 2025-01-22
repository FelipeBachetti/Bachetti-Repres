from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("empresa/<int:id>/", views.company_page, name="company" )
]