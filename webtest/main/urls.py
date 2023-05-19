from django.urls import path, include
from . import views
from .views import image_list, register, login_view


urlpatterns = [
    path(r'^admin_tools/', include('admin_tools.urls')),
    path('', views.index, name='home'),
    path('product', views.product, name='product'),
    path('login', login_view, name='login'),
    path('news', views.news_view, name='news'),
    path('register/', register, name='register'),
    path('contacts', views.contacts, name='contacts'),
    path('images/', image_list, name='image_list'),
    path('plants', views.Plants, name='plants'),
    path('animals', views.Animals, name='animals'),
    path('trade', views.Trade, name='trade'),
    path('chill', views.Chill, name='chill'),


]
