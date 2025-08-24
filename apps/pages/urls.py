from django.urls import path
from apps.pages.views import home_pages_view

app_name = 'pages'

urlpatterns = [
    path('',home_pages_view,name='home')
]