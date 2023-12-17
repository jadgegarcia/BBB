from django.urls import path, include

from . import views
app_name = 'mapper'
urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('signout', views.signout.as_view(), name="signout"),
    path('', views.UserSignUp.as_view(), name='signup'),
    path('signin/', views.UserSignIn.as_view(), name='signin'),
    path('base/', views.Base.as_view(), name="base"),

]

