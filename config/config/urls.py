
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mapper.urls')),
    path('donation/', include('donationbook.urls')),
    path('request/', include('requestbook.urls')),
    path('book/', include('book.urls')),
    path('borrow/', include('borrowbook.urls')),
    path('return/', include('returnbook.urls')),
]
