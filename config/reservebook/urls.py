from django.urls import path
from . import views
app_name='reservebook'
urlpatterns=[
    path('<str:isbn>',views.ReserveBook.as_view(),name="reservebook"),

]