from django.urls import path
import sys
sys.path.append(r'TestWeb\webtest\main')
# sys.path.append(r'C:\Users\abcdefg\Documents\GitHub\TestWeb\webtest\main')
from main.views import register,registration

urlpatterns = [
    path('register/', register, name='register'),
    path('user/registration/', registration, name='reg'),
]