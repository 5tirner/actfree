from rest_framework import response, status, permissions, views
from .serializers import UserInfoSerial
from .passCheck import checkPassword
from .models import UserInfo, UserActivation
import requests
from .codesGenerator import generateCode

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
            codeVerefication = generateCode()
            unactive = UserActivation(email=theData.get('email'), verfCode=codeVerefication)
            unactive.save()
            print(f"Need This Code To Verify Account: {codeVerefication}")
            #TODO: Send Verification Code
            return response.Response(status=status.HTTP_201_CREATED)
        print(f'Failed {serial.error_messages}')
        return response.Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

class login(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    def post(self, req):
        logInfo = req.data
        fetching = requests.post('http://127.0.0.1:10000/authentication/tokens',
                                 json={ 'email': logInfo.get('email'),
                                        'password': logInfo.get('password')
                                       })
        print(f"Status Code == {fetching.status_code}\nContent == {fetching.content}")
        if fetching.status_code != 200:
            return response.Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        userOnDB = UserInfo.objects.get(email=logInfo.get('email'))
        if userOnDB.isAuth == False:
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        myResponse = response.Response(status=status.HTTP_200_OK)
        myResponse.set_cookie(
            'access_token',
            fetching.json().get('access'),
            httponly=True,
            samesite='Strict'
        )
        myResponse.set_cookie(
            'refresh_token',
            fetching.json().get('refresh'),
            httponly=True,
            samesite='Strict'
        )
        return myResponse

class activation(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    def post(self, req):
        try:
            print(f"Email Stored == {req.data.get('email')}")
            userBymail = UserActivation.objects.get(email=req.data.get('email'))
            print(f"User of email: {req.data.get('email')} Send Ativation Code")
            if userBymail.verfCode == req.data.get('activationCode'):
                activateUser = UserInfo.objects.get(email=userBymail.email)
                activateUser.isAuth = True
                activateUser.save()
                userBymail.delete()
                return response.Response(status=status.HTTP_200_OK)
        except:
            print(f"{req.data.get('email')} Not found")
        return response.Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)