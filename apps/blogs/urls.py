from django.urls import path

from apps.blogs.views import blogs_list_view,blogs_detail_view

app_name = 'blogs'

urlpatterns = [
    path('',blogs_list_view,name='list'),
    path('detail/<int:pk>/', blogs_detail_view, name='detail'),
]