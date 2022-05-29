from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('buy/', views.ListBuy.as_view(), name='list-buy'),
    path('buy/<int:id_buy>', views.update_buy, name='update-buy'),
    path('product/', views.ListProduct.as_view(), name='list-product'),
    path('product/<int:id_product>', views.update_product, name='update-product'),
    path('brand/', views.ListBrand.as_view(), name='list-brand'),
    path('brand/<int:id_brand>', views.update_brand, name='update-brand'),
    path('category/', views.ListCategory.as_view(), name='list-category'),
    path('category/<int:id_category>', views.update_category, name='update-category'),
    path('unit/', views.ListUnit.as_view(), name='list-unit'),
    path('unit/<int:id_unit>', views.update_unit, name='update-unit'),
    path('magazine/', views.ListMagazine.as_view(), name='list-magazine'),
    path('magazine/<int:id_magazine>', views.update_magazine, name='update-magazine')
]
