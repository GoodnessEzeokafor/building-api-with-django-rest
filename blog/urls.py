from django.urls import path
from . import views 

urlpatterns = [
    path('posts/', views.PostListCreateAPIView.as_view(), name='api-post-list'),
    path('posts/<uuid:pk>/',views.PostDetailsAPIView.as_view(), name='api-post-details'),
]