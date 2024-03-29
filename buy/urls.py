from . import views
from django.urls import path

from .views import insert_buy

urlpatterns = [
    path('', views.index, name='index'),
    path('price/list/<int:pk>', views.show_list_price, name='list-price'),
    path('price/plot/<int:pk>', views.show_plot_price, name='plot-price'),
    path('buy/', views.show_period_expenses, name='list-buy'),
    path('buy/<int:pk>', views.UpdateBuy.as_view(), name='update-buy'),
    path('buy/del/<int:pk>', views.DeleteBuy.as_view(), name='del-buy'),
    path('buy/new', views.CreateBuy.as_view(), name='create-buy'),
    path('product/', views.ListProduct.as_view(), name='list-product'),
    path('product/<int:pk>', views.UpdateProduct.as_view(), name='update-product'),
    path('product/del/<int:pk>', views.DeleteProduct.as_view(), name='del-product'),
    path('product/new', views.CreateProduct.as_view(), name='create-product'),
    path('brand/', views.ListBrand.as_view(), name='list-brand'),
    path('brand/<int:pk>', views.UpdateBrand.as_view(), name='update-brand'),
    path('brand/del/<int:pk>', views.DeleteBrand.as_view(), name='del-brand'),
    path('brand/new', views.CreateBrand.as_view(), name='create-brand'),
    path('category/', views.ListCategory.as_view(), name='list-category'),
    path('category/<int:pk>', views.UpdateCategory.as_view(), name='update-category'),
    path('category/del/<int:pk>', views.DeleteCategory.as_view(), name='del-category'),
    path('category/new', views.CreateCategory.as_view(), name='create-category'),
    path('unit/', views.ListUnit.as_view(), name='list-unit'),
    path('unit/<int:pk>', views.UpdateUnit.as_view(), name='update-unit'),
    path('unit/new', views.CreateUnit.as_view(), name='create-unit'),
    path('unit/del/<int:pk>', views.DeleteUnit.as_view(), name='del-unit'),
    path('magazine/', views.ListMagazine.as_view(), name='list-magazine'),
    path('magazine/<int:pk>', views.UpdateMagazine.as_view(), name='update-magazine'),
    path('magazine/new', views.CreateMagazine.as_view(), name='create-magazine'),
    path('magazine/del/<int:pk>', views.DeleteMagazine.as_view(), name='del-magazine'),
    path('load_buy/', views.LoadBuy.as_view(), name='load_buy'),
    path('insert/', insert_buy, name='insert_buy'),
]
