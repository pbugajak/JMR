from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.first_html_response, name='index'),
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
