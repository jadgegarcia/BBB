from django.urls import path
from . import views
app_name='returnbook'
urlpatterns=[
    path('<str:username>/',views.ReturnBook.as_view(),name="returnbook"),
    path('<int:borrow_book_id>/', views.AddReturn.as_view(), name="add"),
]