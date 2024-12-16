from rest_framework.serializers import ModelSerializer
from .models import UserInfo, UserActivation

class UserInfoSerial(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['firstname', 'lastname', 'username', 'email', 'password']

class UserActivation(ModuleNotFoundError):
    class Meta:
        model = UserActivation
        fields = ['verfCode']