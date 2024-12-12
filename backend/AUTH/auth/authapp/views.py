from rest_framework import response, status, permissions, views
from .serializers import UserInfoSerial

class SignUp(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    def post(self, req):
        print(f'- Data To Post {req.data}.')
        print('Etat: ')
        serial = UserInfoSerial(data=req.data)
        if serial.is_valid():
            serial.save()
            print('Success')
            return response.Response(status=status.HTTP_201_CREATED)
        print('Failed')
        return response.Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
