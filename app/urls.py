from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', views.MuneCreateView.as_view(), name='munecreate')
]