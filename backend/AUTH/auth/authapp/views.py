from rest_framework import response, status, permissions, views
from .serializers import UserInfoSerial
import json

class SignUp(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    def post(self, req):
        userinfo = req.data
        print(f'- Data To Post {userinfo}.')
        print('Etat: ', end='')
        serial = UserInfoSerial(data=userinfo)
        if serial.is_valid():
            serial.save()
            print('Success')
            return response.Response(status=status.HTTP_201_CREATED)
        print(f'Failed {serial.error_messages}')
        return response.Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
