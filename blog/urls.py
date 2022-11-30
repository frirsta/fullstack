from . import views
from django.urls import path
from .views import AddPostView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
