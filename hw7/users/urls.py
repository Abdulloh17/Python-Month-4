from django.urls import path
from users.views import RegisterView


urlpatterns = [
    path("user/register/", RegisterView.as_view(), name='register')
]