from rest_framework import response, status, decorators, permissions
from .serializers import UserInfoSerial

@decorators.permission_classes([permissions.AllowAny])
@decorators.api_view(["POST"])
@decorators.authentication_classes([])
def sign(req):
    print(f'Infos To Post: {req.data}')
    serial = UserInfoSerial(data=req.data)
    if serial.is_valid():
        serial.save()
        return response.Response(status=status.HTTP_201_CREATED)
    return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)