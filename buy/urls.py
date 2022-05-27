from . import views
from django.urls import path

urlpatterns = [
    path('buy/', views.ListBuy.as_view()),
    path('product/', views.ListProduct.as_view()),
]
