from django.urls import path
from posts.views import hello, index, about, contacts, get_post

urlpatterns = [
    path("hello/", hello, name="hello"),
    path("", index, name="main-page"),
    path("about/", about, name="about-page"),
    path("contacts/", contacts, name="contacts-page"),
    path("post/<int:post_id>/", get_post, name="post-detail"),
]
