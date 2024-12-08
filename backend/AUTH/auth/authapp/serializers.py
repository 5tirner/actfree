from rest_framework.serializers import ModelSerializer
from .models import UserInfo

class UserInfoSerial(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['firstname', 'lastname', 'username', 'email', 'brithdate', 'password']