from django.urls import path
from . import views
app_name = 'donationbook'
urlpatterns = [
    path('', views.donation.as_view(), name="donation"),
    path('donate/', views.donate_book.as_view(), name="donate"),
]