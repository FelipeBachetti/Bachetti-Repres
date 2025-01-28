from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("empresa/<int:id>/", views.company_page, name="company" ),
    path("empresa/<int:id_emp>/tipo/<int:id_tip>/", views.products_page, name="products"),
    path("empresa/<int:id_emp>/tipo/<int:id_tip>/produto/<int:id_pro>/", views.product_page, name="product"),
]