from django.conf.urls import url
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'', IndexView.as_view(), name='index'),
]