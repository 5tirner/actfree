from rest_framework import response, status, permissions, views
from .serializers import UserInfoSerial
from .passCheck import checkPassword
from .models import UserInfo

class SignUp(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    def post(self, req):
        theData = req.data
        print(f'- Data To Post {theData}.')
        print('Etat: ', end='')
        serial = UserInfoSerial(data=theData)
        if serial.is_valid():
            if checkPassword(theData.get('password')) == False:
                return response.Response(status=status.HTTP_204_NO_CONTENT)
            UserInfo.objects.create_user(
                firstname = theData.get('firstname'),
                lastname = theData.get('lastname'),
                username = theData.get('username'),
                email = theData.get('email'),
                password = theData.get('password')
            )
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
            pass
        except:
            return response.Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)