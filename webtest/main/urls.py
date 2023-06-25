from django.urls import path, include
from . import views
from .views import image_list, login_view, card_detail,news_view
from django_email_verification import urls as email_urls
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
    path('news/', news_view, name='news_view'),
    path('animals/<int:card_id>/', views.animal_card, name='animal_card'),
    path('create_order/', views.create_order, name='create_order'),
    path('create_order_ur/', views.create_order_ur, name='create_order_ur'),
    path(r'^admin_tools/', include('admin_tools.urls')),
    path('', views.index, name='home'),
    path('', views.index, name='index'),
    path('product', views.product, name='product'),
    path('news', views.news_view, name='news'),
    path('contacts', views.contacts, name='contacts'),
    path('shop', views.shop, name='shop'),
    path('images/', image_list, name='image_list'),
    path('plants', views.Plants, name='plants'),
    path('animals', views.Animals, name='animals'),
    path('trade', views.Trade, name='trade'),
    path('chill', views.Chill, name='chill'),
    path('user/registration/', views.registration, name='reg'),
    path('email/', include(email_urls)),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(next_page='profile'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('like_article/', views.like_article, name='like_article')



]

handler404 = "main.views.page_not_found_view"