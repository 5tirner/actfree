from rest_framework import response, status, permissions, views
from .serializers import UserInfoSerial
from .passCheck import checkPassword
from .models import UserInfo

class SignUp(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    def post(self, req):
        userinfo = req.data
        print(f'- Data To Post {userinfo}.')
        print('Etat: ', end='')
        serial = UserInfoSerial(data=userinfo)
        if serial.is_valid():
            if checkPassword(userinfo.get('password')) == False:
                return response.Response(status=status.HTTP_204_NO_CONTENT)
            serial.save()
            print('Success')
            #TODO: Send Verification Code
            return response.Response(status=status.HTTP_201_CREATED)
        print(f'Failed {serial.error_messages}')
        return response.Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

class login(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    def post(self, req):
        logInfo = req.data
        try:
            userInDb = UserInfo.objects.get(email=logInfo.get('email'))
            print(f'The Email: {logInfo.get('email')} Stored In DB')
            if userInDb.password != logInfo.get('password'):
                return response.Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            print(f'User Come With The Right Password: {logInfo.get('password')}')
            return response.Response(status=status.HTTP_200_OK)
        except:
            return response.Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)