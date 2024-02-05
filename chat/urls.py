from django.urls import path
from . import views
urlpatterns = [
    path('', views.websocket_test, name='index')
]