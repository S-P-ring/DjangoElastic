from django.contrib import admin
from django.urls import path
from home.views import *


urlpatterns = [
    path('', index),
    path('search/', PublisherDocumentView.as_view({'get': 'list'})),
    path('admin/', admin.site.urls),
]
