from django.urls import path
import sys
sys.path.append(r'C:\Users\Bound\Downloads\TestWeb-main\webtest\main')
# sys.path.append(r'C:\Users\abcdefg\Documents\GitHub\TestWeb\webtest\main')
from views import register

urlpatterns = [
    path('register/', register, name='register'),
]