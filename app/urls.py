from django.urls import path
from . import views
from .views import *

app_name = 'app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', views.home, name='home'),
]