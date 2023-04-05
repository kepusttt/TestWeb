from django.urls import path
import sys
sys.path.append(r'D:\Users\рг\PycharmProjects\test\webtest\main')
from views import register

urlpatterns = [
    path('register/', register, name='register'),
]