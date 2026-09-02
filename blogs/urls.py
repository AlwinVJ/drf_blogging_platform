from django.urls import path

from .views import BlogList, BlogDetails

urlpatterns = [
    path('', BlogList.as_view(), name='blog-list'),
    path('<int:pk>/', BlogDetails.as_view(), name='blog-detail'),
]