from django.urls import path
from . import views
app_name='returnbook'
urlpatterns=[
    path('<str:username>/',views.ReturnBook.as_view(),name="returnbook"),
    #path('<str:borrow_book_id>/', views.AddReturn.as_view(), name="add"),
]