from django.urls import path
from .views import sign
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    #API's
    path('sign', sign),
    #Tokens
    path('tokens', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]