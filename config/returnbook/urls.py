from django.urls import path
from . import views
app_name='returnbook'
urlpatterns=[
    path('', views.ReturnList.as_view(), name="returnlist"),
    path('<str:username>/', views.ReturnBook.as_view(), name="returnbook"),
]