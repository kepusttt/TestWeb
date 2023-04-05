from django.urls import path, include
from . import views
from .views import image_list, register


urlpatterns = [
    path('', views.index, name='home'),
    path('product', views.product, name='product'),
    path('login', views.login, name='login'),
    path('account', views.account, name='account'),
    path('register/', register, name='register'),
    path('images/', image_list, name='image_list'),

]
