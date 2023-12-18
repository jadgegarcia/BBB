from django.urls import path, include
from . import views
app_name = 'book'
urlpatterns = [
    path('', views.Books.as_view(), name="books"),
    path('<str:isbn>', views.Detail.as_view(), name="detail"),
    #path('return/', include('returnbook.urls')),
]