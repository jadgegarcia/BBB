from django.urls import path
from . import views
app_name = 'borrow'
urlpatterns = [
    path('borrow/<str:isbn>/', views.Borrow.as_view(), name="borrow"),
]