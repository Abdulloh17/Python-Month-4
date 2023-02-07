from rest_framework import serializers
from .models import CustomUser

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "is_superuser", "email", "is_staff", "is_active", "date_joined")