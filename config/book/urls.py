from django.urls import path
from . import views
app_name = 'book'
urlpatterns = [
    path('', views.Books.as_view(), name="books"),
    path('<str:isbn>', views.Detail.as_view(), name="detail"),
]