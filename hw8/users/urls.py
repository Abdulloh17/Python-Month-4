from django.urls import path
from users.views import RegisterView, UsersListAPIView


urlpatterns = [
    path("user/register/", RegisterView.as_view(), name='register'),
    path("api/users/list/", UsersListAPIView.as_view(), name='users-list-api'),
]