from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("empresa/<int:id>/", views.company_page, name="company" ),
    path("empresa/<int:id_emp>/tipo/<int:id_tip>/", views.product_page, name="product"),
]