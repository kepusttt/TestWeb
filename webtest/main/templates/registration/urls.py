from django.urls import path
import sys
sys.path.append(r'C:\Users\abcdefg\Desktop\TestWeb-main\webtest\main')
from views import register

urlpatterns = [
    path('register/', register, name='register'),
]