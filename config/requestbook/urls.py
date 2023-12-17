from django.urls import path
from . import views

app_name = 'requestbook'

urlpatterns = [
    path('', views.RequestView.as_view(), name='request'),
    path('request_list/', views.RequestList.as_view(), name='list'),
]