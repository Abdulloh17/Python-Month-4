from django.urls import path
from posts.views import hello, IndexView, about, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, PostListAPIView, PostCreateAPIView

urlpatterns = [
    path("hello/", hello, name="hello"),
    path("", IndexView.as_view(), name="main-page"),
    path("about/", about, name="about-page"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create", PostCreateView.as_view(), name="post-create"),
    path("post/delete/<int:pk>", PostDeleteView.as_view(), name="post-delete"),
    path("post/update/<int:pk>", PostUpdateView.as_view(), name="post-update"),
    path("api/posts/list/", PostListAPIView.as_view(), name="post-list-api"),
    path("api/posts/create/", PostCreateAPIView.as_view(), name="post-create-api"),
] 