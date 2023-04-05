from django.urls import path
from . import views
from .views import image_list


urlpatterns = [
    path('', views.index, name='home'),
    path('product', views.product, name='product'),
    path('login', views.login, name='login'),
    path('images/', image_list, name='image_list')
]
