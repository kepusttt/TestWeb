from django.urls import path
import sys
sys.path.append(r'C:\Users\Bound\Downloads\TestWeb-main\webtest\main')
from views import register

urlpatterns = [
    path('register/', register, name='register'),
]