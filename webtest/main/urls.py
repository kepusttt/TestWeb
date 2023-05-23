from django.urls import path, include
from . import views
from .views import image_list, register, login_view, card_detail,news_view


urlpatterns = [
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
    path('news/', news_view, name='news_view'),
    path('animals/<int:card_id>/', views.animal_card, name='animal_card'),
    path('create_order/', views.create_order, name='create_order'),
    path('create_order_ur/', views.create_order_ur, name='create_order_ur'),
    path(r'^admin_tools/', include('admin_tools.urls')),
    path('', views.index, name='home'),
    path('product', views.product, name='product'),
    path('login', login_view, name='login'),
    path('news', views.news_view, name='news'),
    path('register/', register, name='register'),
    path('contacts', views.contacts, name='contacts'),
    path('shop', views.shop, name='shop'),
    path('images/', image_list, name='image_list'),
    path('plants', views.Plants, name='plants'),
    path('animals', views.Animals, name='animals'),
    path('trade', views.Trade, name='trade'),
    path('chill', views.Chill, name='chill'),


]
